# TrendFusion Data Contract

## Signal

A Signal is the smallest meaningful unit of external evidence.

Required:
- `id`
- `source`
- `title`
- `domain`
- `collected_at`
- `content_hash`

Optional:
- `text`
- `url`
- `published_at`
- `entities`
- `topics`

## Future Trend Contract

```text
trend_id
name
description
domains
momentum
acceleration
signal_count
evidence_ids
market_impact
company_responses
forecast
confidence
created_at
updated_at
```

## Evidence Contract

```text
evidence_id
signal_id
trend_id
claim
source
source_date
relevance_score
```

The evidence layer makes generated explanations traceable.
