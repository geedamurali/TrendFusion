from collections.abc import Iterable

from backend.app.models.signal import Signal


class SignalCollector:
    """Interface implemented by concrete source collectors."""

    name = "base"

    def collect(self) -> Iterable[Signal]:
        raise NotImplementedError


def deduplicate_signals(
    signals: Iterable[Signal],
) -> list[Signal]:
    """Remove duplicate signals using the canonical content hash."""

    unique: dict[str, Signal] = {}

    for signal in signals:
        unique.setdefault(
            signal.content_hash,
            signal,
        )

    return list(unique.values())


def collect_from_source(
    collector: SignalCollector,
) -> list[Signal]:
    """Collect and deduplicate signals from one source."""

    signals = collector.collect()

    return deduplicate_signals(signals)
