from typing import Any, Dict
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from src.domain.ml.ports import ModelRegistry, TrainingDataProvider, ExperimentTracker
from src.application.dtos import TrainRequestDTO, TrainResponseDTO
from src.domain.ml.entities import TrainingJob

class TrainingService:
    def __init__(
        self,
        data_provider: TrainingDataProvider,
        model_registry: ModelRegistry,
        experiment_tracker: ExperimentTracker
    ):
        self.data_provider = data_provider
        self.model_registry = model_registry
        self.experiment_tracker = experiment_tracker

    def train_model(self, request: TrainRequestDTO) -> TrainResponseDTO:
        # Start MLFlow run
        run_id = self.experiment_tracker.start_run(run_name=f"train_{request.model_name}")
        
        try:
            # Load Data
            df = self.data_provider.load_data(request.data_source)
            
            # Simple preprocessing (assuming last column is target for this scaffolding)
            X = df.iloc[:, :-1]
            y = df.iloc[:, -1]
            
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            
            # Log params
            self.experiment_tracker.log_params(request.params)
            
            # Train Model (Simple Logistic Regression for demo)
            model = LogisticRegression(**request.params)
            model.fit(X_train, y_train)
            
            # Evaluate
            predictions = model.predict(X_test)
            accuracy = accuracy_score(y_test, predictions)
            
            # Log metrics
            self.experiment_tracker.log_metrics({"accuracy": accuracy})
            
            # Save Model
            artifact = self.model_registry.save_model(
                model, 
                name=request.model_name, 
                metadata={"accuracy": accuracy, "run_id": run_id}
            )
            
            # Log model to MLFlow
            self.experiment_tracker.log_model(model, "model")
            
            return TrainResponseDTO(
                job_id=run_id,
                status="completed",
                model_uri=artifact.uri
            )
            
        except Exception as e:
            # Log failure
            print(f"Training failed: {e}")
            raise e
        finally:
            self.experiment_tracker.end_run()
