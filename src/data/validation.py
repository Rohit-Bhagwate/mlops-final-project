import pandas as pd
def validate_data(df: pd.DataFrame):

    if df.empty:
        raise ValueError("Dataset is Empty")

    if df.isnull().sum().sum() > 0:
        raise ValueError("Dataset Contains Missing Values")

    print("Dataset Validation Passed")