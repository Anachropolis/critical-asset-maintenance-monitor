from fastapi import FastAPI
from pathlib import Path
import json


app = FastAPI(title="Maintenance Events API",
              description="Returns sample scheduled maintenance events",
              version="1.0")

DATA = Path(__file__).resolve().parents[1] / "data" / "sample_input" / "maintenance_events.json"


@app.get("/maintenance-events")
def get_maintenance_events():
    with DATA.open("r", encoding="utf-8") as file:
        events = json.load(file)

    return events