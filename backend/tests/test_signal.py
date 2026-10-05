from datetime import datetime, timezone

from backend.app.models.signal import Signal, SignalDomain
from backend.ingestion.pipeline import deduplicate_signals


def make_signal(signal_id: str, content_hash: str) -> Signal:
    return Signal(
        id=signal_id,
        source="test",
        title="Example signal",
        text="Example text",
        domain=SignalDomain.NEWS,
        collected_at=datetime.now(timezone.utc),
        content_hash=content_hash,
    )


def test_signal_validation():
    signal = make_signal("sig-1", "hash-1")
    assert signal.domain == SignalDomain.NEWS


def test_signal_deduplication():
    signals = [
        make_signal("sig-1", "same"),
        make_signal("sig-2", "same"),
        make_signal("sig-3", "different"),
    ]

    result = deduplicate_signals(signals)

    assert len(result) == 2
