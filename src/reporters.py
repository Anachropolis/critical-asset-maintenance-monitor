import pandas as pd
from pathlib import Path


class Reporter:

    def generate_csv_report(self, filepath: Path, filename: str, dataset: pd.DataFrame, ) -> None:

        Path.mkdir(filepath, exist_ok=True)
        if filename and not filename.endswith('.csv'):
            filename = filename + '.csv'

        if filename is None:
            filename = "report.csv"

        dataset.to_csv(filepath.joinpath(filename), index=False)
