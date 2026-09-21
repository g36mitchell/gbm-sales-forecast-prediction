import streamlit as st
import pandas as pd
import requests
import os

# BaseUrl for the backend APIs
BACKEND_URL = os.getenv("BACKEND_URL", "http://backend:7860").rstrip("/")

# Set the title of the application
st.title("SuperKart Sales Prediction")
st.subheader("Online prediction")

# Collect user input for sales prediction
Product_MRP = st.number_input("Product MRP", min_value = 31.00, step=0.01, value=147.03, format="%.2f")
Product_Weight = st.number_input("Product Weight", min_value = 4.00, step=0.01, value=12.65, format="%.2f")
Product_Sugar_Content = st.selectbox("Product Sugar Content", ["Low Sugar", "Regular", "No Sugar"])
Product_Allocated_Area = st.number_input("Product Allocated Area", min_value = 0.00, step=0.01, value=0.0688, format="%.4f")
Store_Size = st.selectbox("Store Size", ["Small", "Medium", "High"])
Store_Location_City_Type = st.selectbox("Store Location City Type", ["Tier 1", "Tier 2", "Tier 3"])
Store_Type = st.selectbox("Store Type", ["Supermarket Type2", "Supermarket Type1", "Departmental Store", "Food Mart"])
Product_Id_char = st.selectbox("Product Id char", ["FD", "NC", "DR"])
Product_Type = st.selectbox("Product Type", [
    "Fruits and Vegetables",
    "Snack Foods",
    "Frozen Foods",
    "Dairy",
    "Household",
    "Baking Goods",
    "Canned",
    "Health and Hygiene",
    "Meat",
    "Soft Drinks",
    "Breads",
    "Hard Drinks",
    "Others",
    "Starchy Foods",
    "Breakfast",
    "Seafood"
])

# Convert user input into a DataFrame (no real data sanitization here)
input_data = pd.DataFrame([{
  "Product_Weight": Product_Weight,
  "Product_Sugar_Content": Product_Sugar_Content,
  "Product_Allocated_Area": Product_Allocated_Area,
  "Product_MRP": Product_MRP,
  "Store_Size": Store_Size,
  "Store_Location_City_Type": Store_Location_City_Type,
  "Store_Type": Store_Type,
  "Product_Id_char": Product_Id_char,
  "Product_Type": Product_Type
}])

# Make Prediction when Predict button is selected
if st.button("Predict", type="primary"):
  st.success("Frontend test successful: the button is working.")

