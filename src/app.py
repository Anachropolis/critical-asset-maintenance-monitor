from analyzer import DataAnalyzer
import argparse
from reporters import Reporter
from pathlib import Path


def cli():

    parser = argparse.ArgumentParser(description="""generate a report of events/outages on critical equipment
                                                    with overlapping dates""")

    parser.add_argument("--filepath", help="where the report will be saved")
    parser.add_argument("--critical", action="store_true", help="generates a report of events with critical equipment")
    parser.add_argument("--overlaps", action="store_true", help="generates a report of events that overlap")
    parser.add_argument("--filename", help="the filename to save the report to")

    return parser.parse_args()


def main():
    args = cli()

    filepath = Path(args.filepath)
    filename = args.filename if args.filename else None
    analyzer = DataAnalyzer()
    filtered_report = analyzer.refine_report()
    reporter = Reporter()


    if args.critical:
        reporter.generate_csv_report(filepath=filepath, filename=filename, dataset=filtered_report)

    if args.overlaps:
        overlap_report = analyzer.overlap_report()
        reporter.generate_csv_report(filepath=filepath, filename=filename, dataset=overlap_report)

if __name__ == "__main__":
    main()

