"""
Places Discovery Tool (FINAL – Stable & Robust)

Run:
python -m tools.places_tool
"""

from pathlib import Path
from app.utils.loaders import load_json


# 🔹 Resolve app/data directory safely
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "app" / "data"


def _find_places_file() -> Path:
    """
    Locate places JSON file inside app/data.
    """
    for name in ["places.json", "place.json", "poi.json"]:
        candidate = DATA_DIR / name
        if candidate.exists():
            return candidate

    raise FileNotFoundError(
        f"No places data file found in {DATA_DIR}. "
        f"Expected places.json"
    )


PLACES_DATA_PATH = _find_places_file()


def recommend_places(
    city: str,
    min_rating: float = 4.0,
    limit: int = 5
) -> dict:
    """
    Recommend top places in a city.

    Args:
        city (str): City name
        min_rating (float): Minimum rating filter
        limit (int): Max number of places

    Returns:
        dict: Recommended places
    """

    places = load_json(PLACES_DATA_PATH)

    filtered = [
        p for p in places
        if p.get("city", "").lower() == city.lower()
        and p.get("rating", 0) >= min_rating
    ]

    if not filtered:
        return {
            "status": "not_found",
            "message": f"No places found in {city} with rating ≥ {min_rating}"
        }

    # Sort by rating (high → low)
    sorted_places = sorted(filtered, key=lambda x: x["rating"], reverse=True)

    return {
        "status": "success",
        "city": city,
        "total_places": len(sorted_places[:limit]),
        "places": [
            {
                "name": p["name"],
                "type": p["type"],
                "rating": p["rating"]
            }
            for p in sorted_places[:limit]
        ]
    }


# ✅ Ensures output appears in terminal
if __name__ == "__main__":
    print(recommend_places("Goa", min_rating=4.0, limit=5))
