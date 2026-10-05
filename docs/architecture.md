# TrendFusion Architecture

## Core architecture

```text
Sources
  ↓
Collectors
  ↓
Canonical Signals
  ↓
Validation / Deduplication
  ↓
Storage
  ↓
NLP / Entity / Topic Extraction
  ↓
Semantic Representation
  ↓
Trend Detection
  ↓
Evidence Graph
  ↓
Market Impact
  ↓
Company Response
  ↓
Forecasting
  ↓
Evidence-Grounded Explanation
  ↓
Dashboard
  ↓
Outcome Evaluation
```

### Ingestion
Source-specific collectors retrieve external information and convert it into the canonical `Signal` model.

### Intelligence
Semantic processing, clustering, trend scoring, evidence relationships, impact analysis, and forecasting live here.

### API
FastAPI exposes stable interfaces to the frontend and future clients.

### Frontend
The dashboard consumes the API and does not access the database directly.

### Evaluation
Forecasts are stored and compared with later observed outcomes.

## Design rule

Keep source-specific logic inside collectors. The rest of the system consumes the common Signal contract.
