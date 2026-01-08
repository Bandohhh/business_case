from src.config import DATA_PATH, REQUIRED_COLS 
from src.load_data import load_dataset

# Test to ensure dataset file exists
def test_dataset_file_exists():
    assert DATA_PATH.exists(), f"Expected dataset at {DATA_PATH}"

# Test to ensure required columns exist in the dataset
def test_required_columns_exist():
    df = load_dataset()
    missing = [c for c in REQUIRED_COLS if c not in df.columns]
    assert not missing, f"Missing columns: {missing}"
