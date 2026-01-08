from src.retail_data import load_retail_monthly_feature

# Test to ensure retail loader outputs expected columns
def test_retail_loader_outputs_expected_columns():
    df = load_retail_monthly_feature()
    assert list(df.columns) == ["Month", "RetailIndex"]
