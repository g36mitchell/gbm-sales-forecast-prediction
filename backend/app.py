import numpy as np
import joblib
import pandas as pd
from flask import Flask, request, jsonify

sales_prediction_api = Flask("Sales Forecast Prediction")

# Load the saved model
model_path = "superkart_model.joblib"
model = joblib.load(model_path)

# Define a route for the home page (GET request)
@sales_prediction_api.get('/')
def home():
    """
    This function handles GET requests to the root URL ('/') of the API.
    It returns a simple welcome message.
    """
    return "GBM UT AIML Sales Forecast Prediction API"

# Define an endpoint for a single sales forecast (POST request)
@sales_prediction_api.post('/v1/predict')
def predict_sales_forecast():
    """
    This function handles POST requests to the '/v1/predict' endpoint.
    It expects a JSON payload containing product details and returns
    the predicted sales forecast as a JSON response.
    """
    # Get the JSON data from the request body
    product_data = request.get_json()

    # Extract relevant features from the JSON data
    sample = {
        'Product_Weight': product_data['Product_Weight'],
        'Product_Sugar_Content': product_data['Product_Sugar_Content'],
        'Product_Allocated_Area': product_data['Product_Allocated_Area'],
        'Product_MRP': product_data['Product_MRP'],
        'Store_Size': product_data['Store_Size'],
        'Store_Location_City_Type': product_data['Store_Location_City_Type'],
        'Store_Type': product_data['Store_Type'],
        'Product_Id_char': product_data['Product_Id_char'],
        'Product_Type': product_data['Product_Type']
    }

    # Convert the extracted data into a Pandas DataFrame
    input_data = pd.DataFrame([sample])

    # Make prediction
    predicted_sales_forecast = model.predict(input_data)[0]

    # Return the predicted sales forecast
    return jsonify({'Predicted sales forecast (in dollars)': predicted_sales_forecast})

# Define an endpoint for batch sales forecasts (POST request)
@sales_prediction_api.post('/v1/predict_batch')
def predict_sales_forecast_batch():
    """
    This function handles POST requests to the '/v1/predict_batch' endpoint.
    It expects a CSV payload containing a list of product details and returns
    the predicted sales forecasts for each product as a JSON response.
    """
    # Get the uploaded CSV file from the request
    file = request.files['file']
    
    # Get the CSV data from the request body
    input_data = pd.read_csv(file)

    # Make predictions for the batch of products
    predicted_sales_forecasts = model.predict(input_data).tolist()


    # Return the predicted sales forecasts as a list
    return predicted_sales_forecasts