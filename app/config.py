from pathlib import Path

# Project root directory
BASE_DIR = Path(__file__).resolve().parent

# Data directory (NOT inside app)
DATA_DIR = BASE_DIR / "data"

# Data files
FLIGHTS_DATA_PATH = DATA_DIR / "flights.json"
HOTELS_DATA_PATH = DATA_DIR / "hotels.json"

