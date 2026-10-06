from backend.ingestion.collectors.gdelt import GDELTCollector
from backend.app.models.signal import SignalDomain


def test_gdelt_article_to_signal():
    collector = GDELTCollector(
        query="artificial intelligence",
        max_records=1,
    )

    article = {
        "title": "AI adoption is accelerating",
        "url": "https://example.com/ai-trend",
        "snippet": "Companies are increasingly adopting AI.",
        "seendate": "20261006T120000Z",
    }

    signal = collector._to_signal(article)

    assert signal is not None
    assert signal.title == "AI adoption is accelerating"
    assert str(signal.url) == "https://example.com/ai-trend"
    assert signal.text == "Companies are increasingly adopting AI."
    assert signal.source == "gdelt"
    assert signal.domain == SignalDomain.NEWS
    assert signal.published_at is not None
    assert signal.content_hash
    assert signal.id


def test_gdelt_deduplication():
    collector = GDELTCollector(
        query="artificial intelligence",
    )

    article = {
        "title": "AI adoption is accelerating",
        "url": "https://example.com/ai-trend",
        "snippet": "Companies are increasingly adopting AI.",
        "seendate": "20261006T120000Z",
    }

    signal_1 = collector._to_signal(article)
    signal_2 = collector._to_signal(article)

    assert signal_1 is not None
    assert signal_2 is not None

    result = collector._deduplicate(
        [signal_1, signal_2]
    )

    assert len(result) == 1