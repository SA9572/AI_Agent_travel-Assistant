"""
Hotel Recommendation Tool (FINAL FIXED VERSION)

Run:
python -m tools.hotel_tool
"""

from pathlib import Path
from app.utils.loaders import load_json


# 🔹 Resolve correct path to app/data/hostel.json
PROJECT_ROOT = Path(__file__).resolve().parents[1]
HOTEL_DATA_PATH = PROJECT_ROOT / "app" / "data" / "hotels.json"


def recommend_hotel(city: str, min_stars: int = 3) -> dict:
    hotels = load_json(HOTEL_DATA_PATH)

    matching_hotels = [
        h for h in hotels
        if h["city"].lower() == city.lower()
        and h["stars"] >= min_stars
    ]

    if not matching_hotels:
        return {
            "status": "not_found",
            "message": f"No hotels found in {city} with {min_stars}+ stars"
        }

    best_hotel = min(matching_hotels, key=lambda x: x["price_per_night"])

    return {
        "status": "success",
        "hotel_name": best_hotel["name"],
        "city": best_hotel["city"],
        "stars": best_hotel["stars"],
        "price_per_night": best_hotel["price_per_night"],
        "amenities": best_hotel["amenities"]
    }


# ✅ This guarantees terminal output
if __name__ == "__main__":
    print(recommend_hotel("Goa", min_stars=4))
