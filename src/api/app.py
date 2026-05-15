from fastapi import FastAPI
import joblib
import pandas as pd
app = FastAPI()
# Load model
model = joblib.load("src/model/model.joblib")
@app.get("/")
def home():
    return {"message": "Churn API running"}
@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return {
    "prediction": int(prediction[0])
    }