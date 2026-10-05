# TrendFusion

## AI-Powered Market Trend Intelligence & Forecasting Platform

TrendFusion is an AI-driven market intelligence platform designed to discover emerging trends from weak signals across multiple independent data sources, explain why those trends are emerging, measure their market impact, analyze how major industry players are responding, and forecast how the trends may evolve.

### Core question

> What is emerging, why is it emerging, what has it already changed, how are major companies responding, and where is it likely heading next?

## Product Vision

TrendFusion transforms fragmented public signals into structured market intelligence.

```text
Public Signals
      ↓
Data Collection
      ↓
Cleaning & Normalization
      ↓
Signal Extraction
      ↓
Semantic Understanding
      ↓
Trend Detection
      ↓
Cross-Domain Evidence
      ↓
Market Impact Analysis
      ↓
Company / Industry Response Analysis
      ↓
30 / 60 / 90-Day Forecast
      ↓
Evidence-Based AI Report
      ↓
Prediction vs Reality
```

## Initial Signal Sources

The MVP begins with three complementary signal categories:

1. **News** — current events, industry movement, product launches and public discussion.
2. **Developer activity** — technology adoption and engineering interest.
3. **Research publications** — emerging technical and scientific directions.

Additional sources can be added later without changing the core signal contract.

## MVP Objectives

The first production-oriented version will:

- Collect structured signals from multiple sources.
- Normalize heterogeneous source data into a common schema.
- Remove duplicates and obvious low-quality records.
- Extract entities and topics.
- Represent signals semantically using embeddings.
- Cluster related signals into candidate trends.
- Measure trend momentum and acceleration.
- Build evidence relationships across domains.
- Analyze market impact.
- Track public company responses using verifiable evidence.
- Produce 30/60/90-day forecasts with confidence.
- Store predictions so they can later be compared with actual outcomes.

### Product principle

TrendFusion does **not** claim to predict the future with certainty. Forecasts are estimates supported by historical signals, observed momentum, and evidence.

## Technology Strategy

| Layer | Technology | Purpose |
|---|---|---|
| Language | Python | Data, ML and backend |
| API | FastAPI | Backend service |
| Data processing | Pandas | Cleaning and transformation |
| ML baseline | scikit-learn | Initial models and evaluation |
| Semantic NLP | Sentence Transformers | Signal similarity and clustering |
| Database | PostgreSQL | Structured historical data |
| Vector search | pgvector | Semantic retrieval |
| Graph | NetworkX | Initial evidence graph |
| Forecasting | Feature-based ML + time-series features | Trend forecasting |
| LLM | LLM API | Evidence-grounded explanations |
| Frontend | Next.js | Product dashboard |
| Visualization | Recharts / Plotly | Trend and forecast visualization |
| Packaging | Docker | Reproducible deployment |

We will introduce infrastructure only when the product requires it.

## Repository Structure

```text
TrendFusion/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── models/
│   │   ├── schemas/
│   │   └── main.py
│   ├── ingestion/
│   │   ├── collectors/
│   │   └── pipeline.py
│   └── tests/
├── frontend/
├── data/
│   ├── raw/
│   ├── processed/
│   └── sample/
├── notebooks/
├── docs/
│   ├── architecture.md
│   ├── data-contract.md
│   └── development.md
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

## Getting Started

### Requirements

- Python 3.11+
- Git
- PostgreSQL when persistence is introduced
- Node.js 20+ when the frontend is introduced

### Setup

```bash
git clone <your-repository-url>
cd TrendFusion

python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

macOS/Linux:
```bash
source .venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Copy configuration:
```bash
copy .env.example .env
```

or:
```bash
cp .env.example .env
```

Run the API:
```bash
uvicorn backend.app.main:app --reload
```

Open:
```text
http://127.0.0.1:8000
```

API documentation:
```text
http://127.0.0.1:8000/docs
```

## Development Principles

1. **Evidence before explanation** — AI-generated claims must be grounded in stored evidence.
2. **Rules and models have different jobs** — deterministic rules calculate reproducible metrics; ML detects patterns; LLMs explain evidence.
3. **Build the smallest useful version** — avoid unnecessary infrastructure until the product requires it.
4. **Evaluate continuously** — Prediction → Outcome → Error → Evaluation.
5. **Git regularly** — use small, meaningful commits on the shared `main` branch.

## Initial Milestone

### v0.1 — Foundation

- Repository structure
- Environment configuration
- FastAPI application
- Signal data contract
- Validation models
- Ingestion pipeline interface
- Test foundation
- Architecture documentation

Next: implement the first real signal collector and persistence layer.

## Roadmap

- [x] Project foundation
- [ ] First live data collector
- [ ] Signal normalization
- [ ] Database persistence
- [ ] NLP / embeddings
- [ ] Trend clustering
- [ ] Cross-domain evidence graph
- [ ] Market impact engine
- [ ] Company response intelligence
- [ ] Forecasting engine
- [ ] Prediction vs Reality evaluation
- [ ] Dashboard
- [ ] Deployment
- [ ] v1.0

## Disclaimer

TrendFusion is an analytical and research-oriented system. Forecasts are probabilistic estimates and should not be treated as guaranteed outcomes or financial advice. Public information may be incomplete, delayed, noisy, or contradictory.
