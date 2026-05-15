import os
import pandas as pd
import pickle
import json

def model_fn(model_dir):
    with open(os.path.join(model_dir, "model.pkl"), "rb") as f:
        model = pickle.load(f)
    return model

def input_fn(request_body, request_content_type):
    if request_content_type == "application/json":
        input_data = json.loads(request_body)

        # Convert single JSON object into dataframe
        data = pd.DataFrame([input_data])

        return data
    else:
        raise ValueError(f"Unsupported content type: {request_content_type}")

def predict_fn(input_data, model):
    preds = model.predict(input_data)
    return preds

def output_fn(prediction, content_type):
    return str(prediction.tolist())