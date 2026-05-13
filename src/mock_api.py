from fastapi import FastAPI
from pathlib import Path
import json

#creates an instance of FastAPI
app = FastAPI(title="Maintenance Events API",
              description="Returns sample scheduled maintenance events",
              version="1.0")

DATA = Path("../data/sample_input/maintenance_events.json")

#retrieval function for maintenance events
@app.get("/maintenance-events")
def get_maintenance_events():
    with DATA.open("r", encoding="utf-8") as file:
        events = json.load(file)

    return events