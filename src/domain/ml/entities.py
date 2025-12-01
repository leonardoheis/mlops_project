from datetime import datetime
from typing import Any, Dict, List, Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class ModelArtifact(BaseModel):
    """Represents a trained ML model artifact."""
    id: UUID = Field(default_factory=uuid4)
    name: str
    version: str
    uri: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    metadata: Dict[str, Any] = Field(default_factory=dict)


class TrainingJob(BaseModel):
    """Represents a training job execution."""
    id: UUID = Field(default_factory=uuid4)
    status: str  # e.g., "running", "completed", "failed"
    start_time: datetime = Field(default_factory=datetime.utcnow)
    end_time: Optional[datetime] = None
    params: Dict[str, Any] = Field(default_factory=dict)
    metrics: Dict[str, float] = Field(default_factory=dict)
    model_id: Optional[UUID] = None
    error_message: Optional[str] = None


class PredictionRequest(BaseModel):
    """Represents a request for prediction."""
    features: Dict[str, Any]  # Or a more specific schema if known
    model_name: str
    model_version: Optional[str] = None


class PredictionResult(BaseModel):
    """Represents the result of a prediction."""
    id: UUID = Field(default_factory=uuid4)
    request_id: UUID
    prediction: Any
    probability: Optional[float] = None
    model_version: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
