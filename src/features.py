from .load_data import load_dataset
from .retail_data import load_retail_monthly_feature


def build_features():
    """
    Builds a modelling dataset by combining:
    - Online shopper behaviour 
    - Retail sales index 
    """
    df = load_dataset()
    retail = load_retail_monthly_feature()

    df = df.merge(retail, on="Month", how="left")

    return df
