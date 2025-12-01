from typing import Any, Dict, Optional
from pydantic import BaseModel

class TrainRequestDTO(BaseModel):
    data_source: str
    model_name: str
    params: Dict[str, Any] = {}

class TrainResponseDTO(BaseModel):
    job_id: str
    status: str
    model_uri: Optional[str] = None

class PredictRequestDTO(BaseModel):
    model_name: str
    features: Dict[str, Any]

class PredictResponseDTO(BaseModel):
    prediction: Any
    probability: Optional[float] = None
    model_version: str
