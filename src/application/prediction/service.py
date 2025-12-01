import pandas as pd
from src.domain.ml.ports import ModelRegistry, ModelMonitor
from src.domain.ml.entities import PredictionResult, PredictionRequest
from src.application.dtos import PredictRequestDTO, PredictResponseDTO

class PredictionService:
    def __init__(
        self,
        model_registry: ModelRegistry,
        model_monitor: ModelMonitor
    ):
        self.model_registry = model_registry
        self.model_monitor = model_monitor

    def predict(self, request: PredictRequestDTO) -> PredictResponseDTO:
        # Load model
        model = self.model_registry.get_model(request.model_name)
        artifact = self.model_registry.get_model_artifact(request.model_name)
        
        # Prepare input
        features_df = pd.DataFrame([request.features])
        
        # Predict
        prediction = model.predict(features_df)[0]
        probability = None
        if hasattr(model, "predict_proba"):
            probability = model.predict_proba(features_df)[0].max()
            
        # Create result entity
        result = PredictionResult(
            request_id=artifact.id, # Using artifact ID as dummy request ID link
            prediction=prediction,
            probability=probability,
            model_version=artifact.version
        )
        
        # Log for monitoring
        self.model_monitor.log_prediction(result, features_df)
        
        return PredictResponseDTO(
            prediction=prediction,
            probability=probability,
            model_version=artifact.version
        )
