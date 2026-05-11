from api_client import ApiClient
import utils
import pandas as pd


CLIENT = ApiClient()
EVENT_STATUS_REFERENCE = pd.read_csv("../data/sample_input/event_status_reference.csv")
CRITICAL_ASSETS = pd.read_csv("../data/sample_input/critical_assets.csv")


class DataAnalyzer:

    def __init__(self) -> None:
        self.critical_assets = CRITICAL_ASSETS
        self.event_status_ref = EVENT_STATUS_REFERENCE
        self.maintenance_events = CLIENT.pull_data("maintenance_events")
        self.filtered_events = None

    def refine_report(self):
        scheduled = self.maintenance_events[~(self.maintenance_events["status"].isin(["Completed", "Cancelled", "Deferred"]))]
        critical = scheduled[scheduled["asset_id"].isin(self.critical_assets["asset_id"])]
        filtered_events = critical.merge(self.critical_assets[['asset_id', 'path_role']], on='asset_id', how='left')

        critical_path_overlaps = utils.OverlapTool().run(dataset=filtered_events)

        return critical_path_overlaps





# critical_path_overlaps.to_csv("../data/sample_output/critical_path_overlaps.csv", index=False)
