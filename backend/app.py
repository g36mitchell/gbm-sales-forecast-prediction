import numpy as np
import joblib
import pandas as pd
from flask import Flask, request, jsonify

sales_prediction_api = Flask("Sales Forecast Prediction")

# Load the saved model
model_path = "superkart_model.joblib"
model = joblib.load(model_path)

@sales_prediction_api.get('/')
def home():
  return "GBM UT AIML Sales Forecast Prediction API"  
