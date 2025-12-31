from pathlib import Path
import matplotlib.pyplot as plt

from .load_data import load_dataset


FIG_DIR = Path("figures")


def conversion_rate_by_month():
    """
    Creates a bar chart of conversion rate (Revenue=True) by Month.
    Saves the plot to figures/conversion_rate_by_month.png
    """
    df = load_dataset()

    # Revenue is boolean; mean gives conversion rate
    conv = df.groupby("Month")["Revenue"].mean().sort_values(ascending=False)

    FIG_DIR.mkdir(parents=True, exist_ok=True)

    plt.figure()
    conv.plot(kind="bar")
    plt.ylabel("Conversion rate (Revenue=True)")
    plt.title("Conversion rate by month")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "conversion_rate_by_month.png")
    plt.close()

    print("Saved:", FIG_DIR / "conversion_rate_by_month.png")


if __name__ == "__main__":
    conversion_rate_by_month()
