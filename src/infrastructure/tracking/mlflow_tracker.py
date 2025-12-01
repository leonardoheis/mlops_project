from typing import Any, Dict, Optional
import mlflow
from src.domain.ml.ports import ExperimentTracker


class MLFlowTracker(ExperimentTracker):
    def __init__(self, experiment_name: str, tracking_uri: str = "file:./mlruns"):
        mlflow.set_tracking_uri(tracking_uri)
        mlflow.set_experiment(experiment_name)
        self.active_run = None

    def start_run(self, run_name: Optional[str] = None) -> str:
        self.active_run = mlflow.start_run(run_name=run_name)
        return self.active_run.info.run_id

    def end_run(self):
        mlflow.end_run()
        self.active_run = None

    def log_params(self, params: Dict[str, Any]):
        mlflow.log_params(params)

    def log_metrics(self, metrics: Dict[str, float]):
        mlflow.log_metrics(metrics)

    def log_model(self, model: Any, artifact_path: str):
        mlflow.sklearn.log_model(model, artifact_path)

    def set_tag(self, key: str, value: str):
        mlflow.set_tag(key, value)
