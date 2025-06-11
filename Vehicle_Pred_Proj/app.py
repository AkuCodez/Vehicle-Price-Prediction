import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load the trained model
@st.cache_resource
def load_model():
    return joblib.load("xgboost_vehicle_price_model.pkl")

model = load_model()

# Streamlit UI
st.set_page_config(page_title="Vehicle Price Predictor", layout="centered")
st.title("🚗 Vehicle Price Prediction App")
st.markdown("Enter vehicle details to get the estimated market price.")

# --- User Inputs ---
make = st.text_input("Make (e.g., Toyota, Ford)")
model_name = st.text_input("Model (e.g., Corolla, F-150)")
cylinders = st.number_input("Cylinders", min_value=2, max_value=16, step=1)
fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "Electric", "Hybrid", "CNG"])
mileage = st.number_input("Mileage (in km)", min_value=0)
transmission = st.selectbox("Transmission", ["Automatic", "Manual", "CVT"])
trim = st.text_input("Trim (e.g., XLE, SE, Base)")
body = st.selectbox("Body Type", ["SUV", "Sedan", "Hatchback", "Coupe", "Truck", "Convertible"])
doors = st.selectbox("Number of Doors", [2, 3, 4, 5])
drivetrain = st.selectbox("Drivetrain", ["FWD", "RWD", "AWD", "4WD"])
car_age = st.slider("Car Age (years)", 0, 30)
mileage_per_year = mileage / (car_age if car_age > 0 else 1)

# Prepare data for prediction
input_df = pd.DataFrame([{
    'make': make,
    'model': model_name,
    'cylinders': cylinders,
    'fuel': fuel,
    'mileage': mileage,
    'transmission': transmission,
    'trim': trim,
    'body': body,
    'doors': doors,
    'drivetrain': drivetrain,
    'car_age': car_age,
    'mileage_per_year': mileage_per_year
}])

# Show input data
st.subheader("🔍 Input Summary")
st.write(input_df)

# Predict button
if st.button("🔮 Predict Price"):
    try:
        pred_log_price = model.predict(input_df)[0]
        predicted_price = np.expm1(pred_log_price)
        st.success(f"💰 Estimated Price: ₹{predicted_price:,.0f}")
    except Exception as e:
        st.error(f"Prediction failed. Please check your inputs. ({e})")
