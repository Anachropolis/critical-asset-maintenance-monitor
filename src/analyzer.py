from api_client import ApiClient
import pandas as pd
from pathlib import Path
from utils import DataLoader, OverlapTool, ValidationTool


CLIENT = ApiClient()
EVENT_STATUS_REFERENCE = Path("../data/sample_input/event_status_reference.csv")
CRITICAL_ASSETS = Path("../data/sample_input/critical_assets.csv")
REQUIRED_COLUMNS = {"asset_id", "asset_name", "criticality", "path_role"}


class DataAnalyzer:

    def __init__(self) -> None:
        self.critical_assets = DataLoader().run(file=CRITICAL_ASSETS)
        self.event_status_ref = DataLoader().run(file=EVENT_STATUS_REFERENCE)
        self.maintenance_events = CLIENT.pull_data("maintenance-events")
        self.filtered_events = None


    def refine_report(self) -> pd.DataFrame:
        """Performs validation of critical assets reference file,
           filters event report, and adds equipment criticality
        """
        ValidationTool().run(df=self.critical_assets, required_columns=REQUIRED_COLUMNS, file_label="maintenance_events")

        scheduled = self.maintenance_events[~(self.maintenance_events["status"].isin(["Completed", "Cancelled", "Deferred"]))]
        critical = scheduled[scheduled["asset_id"].isin(self.critical_assets["asset_id"])]
        self.filtered_events = critical.merge(self.critical_assets[["asset_id", "criticality", "path_role"]], on="asset_id", how="left")

        return self.filtered_events


    def overlap_report(self) -> pd.DataFrame:
        # self.filtered_events = self.refine_report() if self.filtered_events is None else self.filtered_events
        critical_path_overlaps = OverlapTool().run(dataset=self.filtered_events)
        return critical_path_overlaps






