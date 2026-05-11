from analyzer import DataAnalyzer
import argparse
from reporters import Reporter
from pathlib import Path


def cli():

    parser = argparse.ArgumentParser(description="""generate a report of events/outages on critical equipment
                                                    with overlapping dates""")

    parser.add_argument("--filepath", help="where the report will be saved")
    parser.add_argument("--run", help="runs the report")

    return parser.parse_args()


args = cli()

filepath = Path(args.filepath)

analyzer = DataAnalyzer()

refined_data = analyzer.refine_report()

Reporter().generate_csv_report(filepath=filepath, dataset=refined_data)
