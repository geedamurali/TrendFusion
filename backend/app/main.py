from fastapi import FastAPI

from backend.app.api.health import router as health_router

app = FastAPI(
    title="TrendFusion API",
    description="Evidence-based market trend intelligence and forecasting API.",
    version="0.1.0",
)

app.include_router(health_router, prefix="/api")


@app.get("/")
def root() -> dict[str, str]:
    return {
        "name": "TrendFusion",
        "version": "0.1.0",
        "status": "foundation-ready",
    }
