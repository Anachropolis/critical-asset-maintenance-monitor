from analyzer import DataAnalyzer
from utils import DataLoader
from api_client import ApiClient
import argparse
from reporters import Reporter
from pathlib import Path
from datetime import datetime



def cli():
    """defines the command-line interface"""

    parser = argparse.ArgumentParser(description="""generate a report of events/outages on critical equipment
                                                    with overlapping dates""")

    parser.add_argument("--output-path", help="where the report will be saved")
    parser.add_argument("--critical", action="store_true", help="generates a report of events with critical equipment")
    parser.add_argument("--overlaps", action="store_true", help="generates a report of events that overlap")
    parser.add_argument("--endpoint", help="the API endpoint to use for requests")
    parser.add_argument("--assets", help="Path to critical assets file")

    return parser.parse_args()


def main():

    client = ApiClient()
    current_date = datetime.now().strftime("%Y-%m-%d")


    # captures cli arguments
    args = cli()

    # set output path
    filepath = Path(args.output_path)


    # set critical event report and overlap report with current date appended
    critical_filename = f"critical_event_report_{current_date}.csv"
    overlap_filename = f"overlap_event_report_{current_date}.csv"


    # retrieve maintenance event report and critical assets in dataframe format
    maintenance_events = client.pull_data(args.endpoint)
    critical_assets = DataLoader().run(Path(args.assets))


    # consolidate maintenance event and critical asset dataframes
    analyzer = DataAnalyzer(maintenance_events=maintenance_events, critical_assets=critical_assets)
    filtered_report = analyzer.refine_report()


    # create a reporter object
    reporter = Reporter()


    # print both reports if nothing selected
    if not args.critical and not args.overlaps:
        args.critical = True
        args.overlaps = True


    # print critical event report
    if args.critical:
        reporter.generate_csv_report(filepath=filepath, filename=critical_filename, dataset=filtered_report)


    # prints overlap event report
    if args.overlaps:
        overlap_report = analyzer.overlap_report()
        reporter.generate_csv_report(filepath=filepath, filename=overlap_filename, dataset=overlap_report)
        print(f"Redundancy overlap events found: {len(overlap_report)}")


    print("\nCritical Asset Maintenance Monitor complete.")
    print(f"Maintenance events pulled from API: {len(maintenance_events)}")
    print(f"Critical asset events found: {len(filtered_report)}")



if __name__ == "__main__":
    main()

