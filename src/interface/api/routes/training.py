from fastapi import APIRouter, Depends, HTTPException
from src.application.dtos import TrainRequestDTO, TrainResponseDTO
from src.application.training.service import TrainingService
from src.infrastructure.ml_registry.filesystem import FileSystemModelRegistry
from src.infrastructure.data.pandas_loader import PandasDataLoader
from src.infrastructure.tracking.mlflow_tracker import MLFlowTracker

router = APIRouter()

def get_training_service():
    return TrainingService(
        data_provider=PandasDataLoader(),
        model_registry=FileSystemModelRegistry(),
        experiment_tracker=MLFlowTracker(experiment_name="default")
    )

@router.post("/train", response_model=TrainResponseDTO)
def train_model(
    request: TrainRequestDTO,
    service: TrainingService = Depends(get_training_service)
):
    try:
        return service.train_model(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
