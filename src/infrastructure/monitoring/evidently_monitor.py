from typing import Any, Optional
import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset, TargetDriftPreset
from evidently.test_suite import TestSuite
from evidently.test_preset import DataDriftTestPreset

from src.domain.ml.entities import PredictionResult
from src.domain.ml.ports import ModelMonitor


class EvidentlyMonitor(ModelMonitor):
    def __init__(self, output_path: str = "./monitoring_reports"):
        self.output_path = output_path
        # Ensure directory exists
        import os
        os.makedirs(output_path, exist_ok=True)

    def log_prediction(
        self,
        prediction_result: PredictionResult,
        features: pd.DataFrame,
        target: Optional[pd.Series] = None
    ):
        # In a real system, we might log this to a database or a file for batch processing later.
        # For this scaffolding, we'll append to a CSV file.
        log_file = f"{self.output_path}/prediction_logs.csv"
        
        # Combine features, prediction, and target
        data = features.copy()
        data['prediction'] = prediction_result.prediction
        if target is not None:
            data['target'] = target
        data['timestamp'] = prediction_result.created_at
        
        # Append to CSV
        header = not os.path.exists(log_file)
        data.to_csv(log_file, mode='a', header=header, index=False)

    def generate_report(self, reference_data: pd.DataFrame, current_data: pd.DataFrame) -> str:
        """Generates an HTML report for data drift."""
        report = Report(metrics=[
            DataDriftPreset(),
            TargetDriftPreset(),
        ])
        
        report.run(reference_data=reference_data, current_data=current_data)
        
        # Save report
        import datetime
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        report_path = f"{self.output_path}/drift_report_{timestamp}.html"
        report.save_html(report_path)
        
        return report_path
