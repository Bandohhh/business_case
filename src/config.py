from pathlib import Path

# File path to the dataset used in the project
DATA_PATH = Path("data/online_shoppers_intention.csv")

# Target column
TARGET_COL = "Revenue"

# Columns we expect to exist (based on the dataset description)
REQUIRED_COLS = [
    "Administrative",
    "Administrative_Duration",
    "Informational",
    "Informational_Duration",
    "ProductRelated",
    "ProductRelated_Duration",
    "BounceRates",
    "ExitRates",
    "PageValues",
    "SpecialDay",
    "Month",
    "OperatingSystems",
    "Browser",
    "Region",
    "TrafficType",
    "VisitorType",
    "Weekend",
    "Revenue",
]
