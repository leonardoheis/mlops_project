from fastapi import APIRouter, Depends, HTTPException
from src.application.dtos import PredictRequestDTO, PredictResponseDTO
from src.application.prediction.service import PredictionService
from src.infrastructure.ml_registry.filesystem import FileSystemModelRegistry
from src.infrastructure.monitoring.evidently_monitor import EvidentlyMonitor

router = APIRouter()

def get_prediction_service():
    return PredictionService(
        model_registry=FileSystemModelRegistry(),
        model_monitor=EvidentlyMonitor()
    )

@router.post("/predict", response_model=PredictResponseDTO)
def predict(
    request: PredictRequestDTO,
    service: PredictionService = Depends(get_prediction_service)
):
    try:
        return service.predict(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
