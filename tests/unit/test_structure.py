from src.domain.ml.entities import ModelArtifact
from src.application.dtos import TrainRequestDTO

def test_imports():
    """Simple test to verify project structure and imports."""
    artifact = ModelArtifact(name="test", version="1", uri="path")
    assert artifact.name == "test"
    
    dto = TrainRequestDTO(data_source="data.csv", model_name="test")
    assert dto.model_name == "test"
