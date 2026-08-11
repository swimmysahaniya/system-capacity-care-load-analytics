from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DATA = PROJECT_ROOT / "data" / "raw" / "HHS_Unaccompanied_Alien_Children_Program.csv"

PROCESSED_DATA = PROJECT_ROOT / "data" / "processed" / "clean_data.csv"

REPORT_PATH = PROJECT_ROOT / "reports"

MODEL_PATH = PROJECT_ROOT / "models"
