import pandas as pd
import os
from src.data.validation import validate_data
from src.data.train import train_model

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def run_pipeline():
    data_path = os.path.join(BASE_DIR, "data","WA_Fn-UseC_-Telco-Customer-Churn.csv")

    df = pd.read_csv(data_path)
    validate_data(df)

    train_model(data_path)

    print("Pipeline completed successfully!")

if __name__ == "__main__":
    run_pipeline()