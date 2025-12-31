import pandas as pd
from pathlib import Path

from .config import DATA_PATH, REQUIRED_COLS


def load_dataset(path: Path = DATA_PATH) -> pd.DataFrame:
    """
    Load the Online Shoppers dataset from a CSV file and validate its schema.
    """
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found at: {path}")

    df = pd.read_csv(path)

    missing = [c for c in REQUIRED_COLS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    return df

