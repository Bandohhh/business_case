from pathlib import Path
import pandas as pd

RETAIL_PATH = Path("data/retail_sales_index.csv")

MONTH_ORDER = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def _find_header_row(filepath: Path) -> int:
    """
    Find the line number (0-indexed) where the real header starts.
    looking for a line containing 'Date' and 'Monthly' (ONS format).
    """
    with filepath.open("r", encoding="utf-8-sig", errors="ignore") as f:
        for i, line in enumerate(f):
            s = line.strip().lower()
            # Skip empty lines
            if not s:
                continue
            # Header line usually contains these
            if "date" in s and "monthly" in s:
                return i
    raise ValueError("Could not find header row containing 'Date' and 'Monthly' in retail_sales_index.csv")


def load_retail_monthly_feature(year_min: int = 2016, year_max: int = 2017) -> pd.DataFrame:
    """
    Load ONS retail sales index CSV and return:
        Month | RetailIndex
    Robust to extra metadata/blank lines before the header.
    """
    if not RETAIL_PATH.exists():
        raise FileNotFoundError(f"Retail dataset not found at: {RETAIL_PATH}")

    header_row = _find_header_row(RETAIL_PATH)

    # Read using the detected header row
    df = pd.read_csv(
        RETAIL_PATH,
        skiprows=header_row,
        header=0,
        encoding="utf-8-sig",
    )

    # Clean column names
    df.columns = [str(c).strip() for c in df.columns]

    # Some ONS files have "3m on 3m " with a trailing space
    # After strip it should be exactly "3m on 3m"
    required = {"Date", "3m on 3m"}
    if not required.issubset(set(df.columns)):
        raise ValueError(f"Expected columns {required} not found. Columns are: {list(df.columns)}")

    # Parse "1997 Jan" style dates (if your file is "Jan 1997" we'll handle below)
    parsed = pd.to_datetime(df["Date"], format="%Y %b", errors="coerce")
    if parsed.isna().mean() > 0.5:
        # fallback for "Jan 1997" style
        parsed = pd.to_datetime(df["Date"], format="%b %Y", errors="coerce")

    df["Date"] = parsed
    df = df.dropna(subset=["Date"])

    df["RetailIndex"] = pd.to_numeric(df["3m on 3m"], errors="coerce")
    df = df.dropna(subset=["RetailIndex"])

    # Align with shopper dataset period
    df = df[(df["Date"].dt.year >= year_min) & (df["Date"].dt.year <= year_max)].copy()

    df["Month"] = df["Date"].dt.strftime("%b")

    out = df.groupby("Month", as_index=False)["RetailIndex"].mean()

    out["Month"] = pd.Categorical(out["Month"], categories=MONTH_ORDER, ordered=True)
    out = out.sort_values("Month").reset_index(drop=True)

    return out
