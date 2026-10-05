from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, HttpUrl


class SignalDomain(str, Enum):
    NEWS = "news"
    DEVELOPER = "developer"
    RESEARCH = "research"
    JOBS = "jobs"
    COMPANY = "company"
    SEARCH = "search"
    OTHER = "other"


class Signal(BaseModel):
    """Canonical representation of an external market signal."""

    id: str = Field(..., description="Stable internal signal identifier.")
    source: str = Field(..., min_length=1)
    title: str = Field(..., min_length=1)
    text: str = Field(default="")
    url: HttpUrl | None = None
    published_at: datetime | None = None
    domain: SignalDomain
    entities: list[str] = Field(default_factory=list)
    topics: list[str] = Field(default_factory=list)
    collected_at: datetime
    content_hash: str = Field(..., min_length=1)
