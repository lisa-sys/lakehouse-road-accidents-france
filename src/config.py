from pathlib import Path

# Project root
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Selected year for the first version of the project
YEAR = 2020

# Data paths
DATA_PATH = PROJECT_ROOT / "data"
RAW_PATH = DATA_PATH / "raw"
BRONZE_PATH = DATA_PATH / "bronze"
SILVER_PATH = DATA_PATH / "silver"
GOLD_PATH = DATA_PATH / "gold"

# Raw files
RAW_FILES = {
    "caracteristiques": RAW_PATH / f"caracteristiques-{YEAR}.csv",
    "lieux": RAW_PATH / f"lieux-{YEAR}.csv",
    "usagers": RAW_PATH / f"usagers-{YEAR}.csv",
    "vehicules": RAW_PATH / f"vehicules-{YEAR}.csv",
}