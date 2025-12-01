import pandas as pd
from src.domain.ml.ports import TrainingDataProvider
from src.domain.ml.exceptions import DataLoadingError

class PandasDataLoader(TrainingDataProvider):
    def load_data(self, source: str) -> pd.DataFrame:
        try:
            if source.endswith(".csv"):
                return pd.read_csv(source)
            elif source.endswith(".parquet"):
                return pd.read_parquet(source)
            elif source.endswith(".json"):
                return pd.read_json(source)
            else:
                raise DataLoadingError(f"Unsupported file format for source: {source}")
        except Exception as e:
            raise DataLoadingError(f"Failed to load data from {source}: {str(e)}")
