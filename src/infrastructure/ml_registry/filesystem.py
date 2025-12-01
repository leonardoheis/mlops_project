import os
import pickle
from typing import Any, Dict, Optional
from datetime import datetime
from uuid import uuid4

from src.domain.ml.entities import ModelArtifact
from src.domain.ml.ports import ModelRegistry
from src.domain.ml.exceptions import ModelNotFoundError


class FileSystemModelRegistry(ModelRegistry):
    def __init__(self, base_path: str = "./models"):
        self.base_path = base_path
        os.makedirs(base_path, exist_ok=True)

    def save_model(self, model: Any, name: str, metadata: Dict[str, Any]) -> ModelArtifact:
        version = datetime.now().strftime("%Y%m%d%H%M%S")
        model_dir = os.path.join(self.base_path, name, version)
        os.makedirs(model_dir, exist_ok=True)
        
        model_path = os.path.join(model_dir, "model.pkl")
        with open(model_path, "wb") as f:
            pickle.dump(model, f)
            
        artifact = ModelArtifact(
            name=name,
            version=version,
            uri=model_path,
            metadata=metadata
        )
        
        # Save artifact metadata
        with open(os.path.join(model_dir, "metadata.pkl"), "wb") as f:
            pickle.dump(artifact, f)
            
        return artifact

    def get_model(self, name: str, version: Optional[str] = None) -> Any:
        artifact = self.get_model_artifact(name, version)
        with open(artifact.uri, "rb") as f:
            return pickle.load(f)

    def get_model_artifact(self, name: str, version: Optional[str] = None) -> ModelArtifact:
        model_base_dir = os.path.join(self.base_path, name)
        if not os.path.exists(model_base_dir):
             raise ModelNotFoundError(name)
             
        if version is None:
            # Get latest version (lexicographically last)
            versions = sorted(os.listdir(model_base_dir))
            if not versions:
                raise ModelNotFoundError(name)
            version = versions[-1]
            
        version_dir = os.path.join(model_base_dir, version)
        metadata_path = os.path.join(version_dir, "metadata.pkl")
        
        if not os.path.exists(metadata_path):
            raise ModelNotFoundError(name, version)
            
        with open(metadata_path, "rb") as f:
            return pickle.load(f)
