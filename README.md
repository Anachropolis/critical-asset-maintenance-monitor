# Critical Asset Maintenance Monitor

A Python API-to-report automation demo that identifies scheduled maintenance events affecting critical assets and detects overlapping maintenance windows that may reduce operational redundancy.

This project demonstrates a practical operations automation pattern: pulling structured event data from an API, comparing it against a critical asset reference list, applying business rules, and generating clean exception reports for review.

The data in this project is fictional and sanitized, but the workflow is modeled after real operational monitoring and outage-review processes where accuracy, timing, and repeatable reporting matter.

---

## Overview

Operations teams often need to review scheduled maintenance, outage, or work activity against a list of important assets.

The manual process usually looks like this:

1. Pull scheduled event data from a system or API.
2. Compare the affected assets against an internal critical asset list.
3. Identify events involving high-priority or operationally important assets.
4. Check whether multiple redundant paths or assets are affected during overlapping time windows.
5. Generate a report for review.

This project automates that workflow.

---

## Business Problem

Scheduled work can create operational risk when it affects critical assets or when multiple related assets are taken out of service during overlapping time windows.

Manually reviewing event lists against critical asset references is repetitive and error-prone, especially when:

- Event data comes from an external API or system.
- Critical asset data is maintained separately.
- Events must be compared by date range.
- Redundancy groups or alternate paths need to be considered.
- Reviewers need a clean exception report rather than a raw data dump.

This tool reduces manual review by automatically identifying the scheduled events most likely to require attention.

---

## Solution

The tool performs the following workflow:

1. Starts with a mock FastAPI service that simulates an external maintenance event API.
2. Pulls scheduled maintenance event data from the API.
3. Loads a local critical asset reference file.
4. Filters events based on status.
5. Identifies scheduled events affecting critical assets.
6. Detects overlapping events within the same redundancy group.
7. Generates CSV reports for review.

The goal is not to replace human operational judgment. The goal is to reduce manual filtering and help reviewers focus on events that may require closer review.

---

## Features

- Mock FastAPI endpoint for scheduled maintenance events.
- API client that pulls JSON data and converts it into a pandas DataFrame.
- Critical asset matching using an internal CSV reference file.
- Event filtering by status.
- Redundancy group overlap detection.
- CSV report generation.
- Input validation for required columns.
- Modular project structure for easier maintenance and testing.

---

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Requests
- pandas
- argparse
- pathlib

---

## Project Structure

```text
critical-asset-maintenance-monitor/
│
├── src/
│   ├── app.py
│   ├── mock_api.py
│   ├── api_client.py
│   ├── analyzer.py
│   ├── reporters.py
│   └── utils.py
│
├── data/
│   ├── sample_input/
│   │   ├── maintenance_events.json
│   │   ├── critical_assets.csv
│   │   └── event_status_reference.csv
│   │
│   └── sample_output/
│
├── docs/
│   └── screenshots/
│
├── README.md
├── requirements.txt
└── .gitignore