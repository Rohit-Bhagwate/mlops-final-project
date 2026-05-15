import joblib
import pandas as pd

def model_fn(model_dir):
    return joblib.load(f"{model_dir}/model.joblib")

def input_fn(request_body, request_content_type):
    data = pd.read_json(request_body)
    return data

def predict_fn(input_data, model):
    preds = model.predict(input_data)
    return preds

def output_fn(prediction, content_type):
    return str(prediction.tolist())