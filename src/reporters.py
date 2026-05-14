import pandas as pd
from pathlib import Path


class Reporter:

    def generate_csv_report(self, filepath: Path, filename: str, dataset: pd.DataFrame, ) -> Path:
        """generates a CSV report from given filepath and filename"""
        filepath.mkdir(parents=True, exist_ok=True)
        output_path = filepath / filename
        dataset.to_csv(output_path, index=False)

        return output_path
