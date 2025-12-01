class DomainException(Exception):
    """Base exception for domain layer."""
    pass


class ModelNotFoundError(DomainException):
    """Raised when a requested model is not found."""
    def __init__(self, name: str, version: str = "latest"):
        super().__init__(f"Model '{name}' (version: {version}) not found.")


class DataLoadingError(DomainException):
    """Raised when data cannot be loaded."""
    pass


class TrainingError(DomainException):
    """Raised when model training fails."""
    pass
