from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
import pandas as pd

from src.domain.ml.entities import ModelArtifact, PredictionResult, TrainingJob


class ModelRegistry(ABC):
    """Interface for persisting and retrieving models."""

    @abstractmethod
    def save_model(self, model: Any, name: str, metadata: Dict[str, Any]) -> ModelArtifact:
        pass

    @abstractmethod
    def get_model(self, name: str, version: Optional[str] = None) -> Any:
        pass

    @abstractmethod
    def get_model_artifact(self, name: str, version: Optional[str] = None) -> ModelArtifact:
        pass


class TrainingDataProvider(ABC):
    """Interface for loading training data."""

    @abstractmethod
    def load_data(self, source: str) -> pd.DataFrame:
        pass


class ExperimentTracker(ABC):
    """Interface for tracking experiments (e.g., MLFlow)."""

    @abstractmethod
    def start_run(self, run_name: Optional[str] = None) -> str:
        pass

    @abstractmethod
    def end_run(self):
        pass

    @abstractmethod
    def log_params(self, params: Dict[str, Any]):
        pass

    @abstractmethod
    def log_metrics(self, metrics: Dict[str, float]):
        pass

    @abstractmethod
    def log_model(self, model: Any, artifact_path: str):
        pass

    @abstractmethod
    def set_tag(self, key: str, value: str):
        pass


class ModelMonitor(ABC):
    """Interface for monitoring model performance and drift (e.g., Evidently)."""

    @abstractmethod
    def log_prediction(
        self,
        prediction_result: PredictionResult,
        features: pd.DataFrame,
        target: Optional[pd.Series] = None
    ):
        pass

    @abstractmethod
    def generate_report(self, reference_data: pd.DataFrame, current_data: pd.DataFrame) -> Any:
        pass
