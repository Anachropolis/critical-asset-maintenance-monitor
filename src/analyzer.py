import api_client
import pandas as pd


client = api_client.ApiClient()

critical_assets = pd.read_csv("../data/sample_input/critical_assets.csv")
event_status_ref = pd.read_csv("../data/sample_input/event_status_reference.csv")
maintenance_events = client.pull_data("maintenance_events")


# print(maintenance_events)
scheduled = maintenance_events[(maintenance_events["status"] != "Completed") & (maintenance_events["status"] != "Cancelled") & (maintenance_events["status"] != "Deferred")]
critical = scheduled[scheduled["asset_id"].isin(critical_assets["asset_id"])]

critical_w_paths = critical.merge(critical_assets[['asset_id', 'path_role']], on='asset_id', how='left')

path_a_work = critical_w_paths[critical_w_paths["path_role"] == "A"]
path_b_work = critical_w_paths[critical_w_paths["path_role"] == "B"]

event_list = []

for entry in path_a_work.iterrows():
    for entry2 in path_b_work.iterrows():
        if (entry[1]["scheduled_start"] <= entry2[1]["scheduled_end"] and
                entry2[1]["scheduled_start"] <= entry[1]["scheduled_end"]):
            event_list.append(entry[1]["event_id"])
            event_list.append(entry2[1]["event_id"])



critical_w_paths_new = critical_w_paths[critical_w_paths["event_id"].isin(event_list)]

critical_w_paths_new.to_csv("../data/sample_output/refined_critical_assets_2.csv", index=False)
