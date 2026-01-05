from pathlib import Path
import pandas as pd

RETAIL_PATH = Path("data/retail_sales_index.csv")

MONTH_ORDER = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]


def load_retail_monthly_feature(
    year_min: int = 2016,
    year_max: int = 2017
) -> pd.DataFrame:
    """
    Load and clean ONS retail sales index data and return:
        Month | RetailIndex
    """
    if not RETAIL_PATH.exists():
        raise FileNotFoundError(f"Retail dataset not found at: {RETAIL_PATH}")

    # Read raw file (real header is first row)
    raw = pd.read_csv(RETAIL_PATH, header=None)

    # First row contains the real column names
    raw.columns = raw.iloc[0]
    df = raw.iloc[1:].copy()

    # Rename columns explicitly
    df = df.rename(columns={
        "Date": "Date",
        "3m on 3m": "RetailIndex"
    })

    # Parse date
    df["Date"] = pd.to_datetime(df["Date"], format="%Y %b", errors="coerce")
    df = df.dropna(subset=["Date"])

    # Convert RetailIndex to numeric
    df["RetailIndex"] = pd.to_numeric(df["RetailIndex"], errors="coerce")
    df = df.dropna(subset=["RetailIndex"])

    # Filter to match online shoppers period
    df = df[(df["Date"].dt.year >= year_min) & (df["Date"].dt.year <= year_max)]

    # Extract month
    df["Month"] = df["Date"].dt.strftime("%b")

    # Aggregate to month-level
    out = (
        df.groupby("Month", as_index=False)["RetailIndex"]
        .mean()
    )

    # Ensure calendar order
    out["Month"] = pd.Categorical(out["Month"], categories=MONTH_ORDER, ordered=True)
    out = out.sort_values("Month").reset_index(drop=True)

    return out
