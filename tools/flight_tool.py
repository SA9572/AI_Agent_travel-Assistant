from datetime import datetime
from app.config import FLIGHTS_DATA_PATH
from app.utils.loaders import load_json


def search_flight(source: str, destination: str) -> dict:
    if source.lower() == destination.lower():
        return {
            "status": "skipped",
            "reason": "Local trip – no flight required"
        }

    flights = load_json(FLIGHTS_DATA_PATH)

    matches = [
        f for f in flights
        if f["from"].lower() == source.lower()
        and f["to"].lower() == destination.lower()
    ]

    if not matches:
        return {"status": "not_found"}

    best = min(matches, key=lambda x: x["price"])

    dep = datetime.fromisoformat(best["departure_time"])
    arr = datetime.fromisoformat(best["arrival_time"])

    return {
        "status": "success",
        "airline": best["airline"],
        "price": best["price"],
        "duration_hours": round((arr - dep).total_seconds() / 3600, 2)
    }
