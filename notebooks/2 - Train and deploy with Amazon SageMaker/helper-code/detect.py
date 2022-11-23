import argparse
import os
import platform
import sys
import torch
import json
import numpy as np
import cv2

def model_fn(model_dir):
    os.system("pip install seaborn")
    torch.hub._validate_not_a_forked_repo=lambda a,b,c: True 
    model = torch.hub.load("ultralytics/yolov5", "custom", path="/opt/ml/model/exp/weights/best.pt", force_reload=True)
    print("Model Loaded")
    return model

def input_fn(input_data, content_type):

    if content_type in ['image/png','image/jpeg']:
        img = np.frombuffer(input_data, dtype=np.uint8)
        img = cv2.imdecode(img, cv2.IMREAD_COLOR)[..., ::-1]
        img = cv2.resize(img, [640,640])
        return img 
    else:
        raise Exception('Requested unsupported ContentType in Accept: ' + content_type)
        return

def predict_fn(input_data, model):
    print("Making inference")
    results = model(input_data)
    print(results)
    df = results.pandas().xyxy[0]
    return(df.to_json(orient="split"))