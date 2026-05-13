import pandas as pd
import api_client
from pathlib import Path

client = api_client.ApiClient()


class OverlapTool:

    def run(self, dataset: pd.DataFrame) -> pd.DataFrame:

        subset_1 = dataset[dataset["path_role"] == "A"]
        subset_2 = dataset[dataset["path_role"] == "B"]
        event_list = []

        for entry in subset_1.iterrows():
            for entry2 in subset_2.iterrows():
                if (entry[1]["scheduled_start"] <= entry2[1]["scheduled_end"] and
                        entry2[1]["scheduled_start"] <= entry[1]["scheduled_end"]):
                    event_list.append(entry[1]["event_id"])
                    event_list.append(entry2[1]["event_id"])

        return dataset[dataset["event_id"].isin(event_list)]



class ValidationTool:

    def run(self, df: pd.DataFrame, required_columns: set[str], file_label: str) -> None:
        """Validate the columns present in the dataframe"""
        missing = required_columns - set(df.columns)

        if missing:
            raise ValueError(
                f"{file_label} is missing required columns: {', '.join(sorted(missing))}"
            )


class DataLoader:

    def run(self, file: Path) -> pd.DataFrame:
        return pd.read_csv(file)








