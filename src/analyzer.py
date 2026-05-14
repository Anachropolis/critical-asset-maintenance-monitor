import pandas as pd
from utils import OverlapTool, ValidationTool


EVENT_REQUIRED_COLUMNS = {
    "event_id",
    "asset_id",
    "asset_name",
    "scheduled_start",
    "scheduled_end",
    "event_type",
    "status",
    "description"
}

CRITICAL_ASSET_REQUIRED_COLUMNS = {
    "asset_id",
    "asset_name",
    "criticality",
    "redundancy_group",
    "path_role"
}




class DataAnalyzer:

    def __init__(self, maintenance_events: pd.DataFrame, critical_assets: pd.DataFrame) -> None:
        self.critical_assets = critical_assets
        self.maintenance_events = maintenance_events
        self.filtered_events = None


    def refine_report(self) -> pd.DataFrame:
        """Performs validation of critical assets reference file,
           filters event report, and adds equipment criticality
        """
        ValidationTool().run(df=self.maintenance_events, required_columns=EVENT_REQUIRED_COLUMNS, file_label="maintenance_events")
        ValidationTool().run(df=self.critical_assets, required_columns=CRITICAL_ASSET_REQUIRED_COLUMNS, file_label="critical assets")

        events = self.maintenance_events.copy()
        assets = self.critical_assets.copy()

        events["asset_id"] = events["asset_id"].astype(str).str.strip()
        assets["asset_id"] = assets["asset_id"].astype(str).str.strip()

        events["scheduled_start"] = pd.to_datetime(events["scheduled_start"])
        events["scheduled_end"] = pd.to_datetime(events["scheduled_end"])

        scheduled = events[~(events["status"].isin(["Completed", "Cancelled", "Deferred"]))].copy()
        critical = scheduled[scheduled["asset_id"].isin(self.critical_assets["asset_id"])].copy()
        filtered = critical.merge(assets[["asset_id", "criticality", "path_role", "redundancy_group"]], on="asset_id", how="left")
        self.filtered_events = filtered[["criticality",
                                         "event_id",
                                        "asset_id",
                                        "asset_name",
                                        "scheduled_start",
                                        "scheduled_end",
                                        "event_type",
                                        "status",
                                        "description",
                                        "path_role",
                                        "redundancy_group"]]

        return self.filtered_events


    def overlap_report(self) -> pd.DataFrame:
        """Compares maintenance events and generates a report
        showing any conflicts affecting redundant resources"""
        self.filtered_events = self.refine_report() if self.filtered_events is None else self.filtered_events
        critical_path_overlaps = OverlapTool().run(dataset=self.filtered_events)
        return critical_path_overlaps




