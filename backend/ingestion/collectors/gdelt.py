from __future__ import annotations

import hashlib
import time
from datetime import datetime, timezone

import httpx

from backend.app.models.signal import Signal, SignalDomain


class GDELTCollector:
    """Collect and normalize news signals from GDELT DOC 2.0."""

    BASE_URL = "https://api.gdeltproject.org/api/v2/doc/doc"

    def __init__(
        self,
        query: str,
        max_records: int = 50,
        timespan: str = "7d",
        timeout: float = 30.0,
    ) -> None:
        self.query = query
        self.max_records = max_records
        self.timespan = timespan
        self.timeout = timeout

    def collect(self) -> list[Signal]:
        """Fetch GDELT articles and convert them into TrendFusion Signals."""

        params = {
            "query": self.query,
            "mode": "artlist",
            "format": "json",
            "maxrecords": self.max_records,
            "timespan": self.timespan,
            "sort": "datedesc",
        }

        for attempt in range(3):
            response = httpx.get(
                self.BASE_URL,
                params=params,
                timeout=self.timeout,
            )

            if response.status_code == 429:
                wait_seconds = 10 * (attempt + 1)

                print(
                    f"GDELT rate limit reached. "
                    f"Retrying in {wait_seconds} seconds..."
                )

                time.sleep(wait_seconds)
                continue

            response.raise_for_status()
            break

        else:
            raise RuntimeError(
                "GDELT rate limit persisted after 3 attempts."
            )

        data = response.json()

        signals: list[Signal] = []

        for article in data.get("articles", []):
            signal = self._to_signal(article)

            if signal is not None:
                signals.append(signal)

        return self._deduplicate(signals)

    def _to_signal(self, article: dict) -> Signal | None:
        """Convert one GDELT article into the TrendFusion Signal contract."""

        title = str(article.get("title", "")).strip()
        url = str(article.get("url", "")).strip()

        if not title or not url:
            return None

        text = str(article.get("snippet", "")).strip()

        published_at = self._parse_date(
            article.get("seendate")
        )

        content = f"{title}\n{text}".strip()

        content_hash = hashlib.sha256(
            content.lower().encode("utf-8")
        ).hexdigest()

        signal_id = hashlib.sha256(
            url.encode("utf-8")
        ).hexdigest()

        return Signal(
            id=signal_id,
            source="gdelt",
            title=title,
            text=text,
            url=url,
            published_at=published_at,
            domain=SignalDomain.NEWS,
            entities=[],
            topics=[],
            collected_at=datetime.now(timezone.utc),
            content_hash=content_hash,
        )

    @staticmethod
    def _parse_date(value: object) -> datetime | None:
        """Parse GDELT's publication date format."""

        if not value:
            return None

        value = str(value)

        try:
            return datetime.strptime(
                value,
                "%Y%m%dT%H%M%SZ",
            ).replace(tzinfo=timezone.utc)

        except ValueError:
            return None

    @staticmethod
    def _deduplicate(
        signals: list[Signal],
    ) -> list[Signal]:
        """Remove duplicate signals by content hash."""

        unique: dict[str, Signal] = {}

        for signal in signals:
            unique.setdefault(
                signal.content_hash,
                signal,
            )

        return list(unique.values())