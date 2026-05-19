import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import mlflow
import os
import boto3
import pickle


#mlflow.set_tracking_uri("http://13.126.138.113:5000")

def train_model(data_path):
    mlflow.set_experiment("churn_simple")
    df = pd.read_csv(data_path)

    # -----------------------
    # DATA CLEANING
    # -----------------------
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors='coerce')
    df = df.drop("customerID", axis=1)
    df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})
    df = df.dropna()

    X = df.drop("Churn", axis=1)
    y = df["Churn"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # -----------------------
    # PREPROCESSING
    # -----------------------
    cat_cols = X.select_dtypes(include=['object']).columns
    num_cols = X.select_dtypes(exclude=['object']).columns

    preprocessor = ColumnTransformer([
        ("num", StandardScaler(), num_cols),
        ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols)
    ])

    pipeline = Pipeline([
        ("prep", preprocessor),
        ("model", LogisticRegression(max_iter=1000))
    ])

    # -----------------------
    # TRAINING
    # -----------------------
    with mlflow.start_run():

        pipeline.fit(X_train, y_train)

        preds = pipeline.predict(X_test)
        acc = accuracy_score(y_test, preds)

        mlflow.log_metric("accuracy", acc)

        print("Accuracy:", acc)

        # -----------------------
        # SAVE MODEL (SAFE FORMAT)
        # -----------------------
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        model_dir = os.path.join(BASE_DIR, "model")
        os.makedirs(model_dir, exist_ok=True)

        model_path = os.path.join(model_dir, "model.pkl")

        with open(model_path, "wb") as f:
            pickle.dump(pipeline, f)

        print("Model saved at:", model_path)

        # -----------------------
        # UPLOAD TO S3
        # -----------------------
        s3 = boto3.client("s3")
        bucket_name = "mlops-project-churn-customer-bucket-prod"

        s3.upload_file(
            model_path,
            bucket_name,
            "model/model.pkl"
        )

        print("Uploaded model to S3")
    print(os.path.abspath(__file__))
    print(BASE_DIR)
    return model_path

