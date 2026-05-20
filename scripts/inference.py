import joblib
import pandas as pd
import json
import os

def model_fn(model_dir):
    model_path = os.path.join(model_dir, "model.pkl")
    model = joblib.load(model_path)
    return model

def input_fn(request_body, request_content_type):
    data = json.loads(request_body)
    df = pd.DataFrame([data])
    return df

def predict_fn(input_data, model):
    prediction = model.predict(input_data)
    return prediction

def output_fn(prediction, content_type):
    return json.dumps({
        "prediction": int(prediction[0])
    })