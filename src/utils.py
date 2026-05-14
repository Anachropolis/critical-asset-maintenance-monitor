import pandas as pd
from pathlib import Path



class OverlapTool:

    def run(self, dataset: pd.DataFrame) -> pd.DataFrame:
        """checks for overlaps between redundant resources"""

        event_list = []

        for group_name, group_df in dataset.groupby("redundancy_group"):
            subset_1 = group_df[group_df["path_role"] == "A"]
            subset_2 = group_df[group_df["path_role"] == "B"]


            for entry in subset_1.iterrows():
                for entry2 in subset_2.iterrows():
                    if (entry[1]["scheduled_start"] <= entry2[1]["scheduled_end"] and
                            entry2[1]["scheduled_start"] <= entry[1]["scheduled_end"]):
                        event_list.append(entry[1]["event_id"])
                        event_list.append(entry2[1]["event_id"])

        overlaps = dataset[dataset["event_id"].isin(event_list)].copy()
        overlaps = overlaps[["redundancy_group", "event_id", "event_type", "asset_id", "path_role", "scheduled_start", "scheduled_end"]]


        return overlaps



class ValidationTool:

    def run(self, df: pd.DataFrame, required_columns: set[str], file_label: str) -> None:
        """Validates the columns present in the dataframe"""
        missing = required_columns - set(df.columns)

        if missing:
            raise ValueError(
                f"{file_label} is missing required columns: {', '.join(sorted(missing))}"
            )


class DataLoader:

    def run(self, file: Path) -> pd.DataFrame:
        """Loads data from csv files"""
        return pd.read_csv(file)


