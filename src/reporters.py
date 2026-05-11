import pandas as pd
from pathlib import Path


class Reporter:

    def generate_csv_report(self, filepath: Path, dataset: pd.DataFrame, filename: str ="critical_path_overlaps.csv") -> None:

        Path.mkdir(filepath, exist_ok=True)
        full_path = filepath / filename
        dataset.to_csv(full_path, index=False)