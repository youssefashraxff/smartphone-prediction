import streamlit as st
import joblib
import pandas as pd

# Load trained objects
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "phonePred.pkl")

artifacts = joblib.load(MODEL_PATH)

pipeline = artifacts["pipeline"]
label_encoder = artifacts["label_encoder"]
features_list = artifacts["features"]

st.set_page_config(page_title="Smartphone Price Prediction", layout="centered")

st.title("📱 Smartphone Price Prediction")

st.markdown("Enter the smartphone specifications below to predict the **price category**.")

# 🏆 Selected Features
clock_speed = st.number_input("Clock Speed (GHz)", min_value=0.0, format="%.2f")
nfc_selection = st.radio("NFC Support", ["Yes", "No"])
rating = st.number_input("Rating", min_value=0.0, max_value=100.0, format="%.1f")
ppi = st.number_input("PPI", min_value=0.0, format="%.2f")
fast_charging = st.number_input("Fast Charging Power (W)", min_value=0.0, format="%.1f")
storage = st.number_input("Storage Size (GB)", min_value=0.0, format="%.1f")
refresh_rate = st.number_input("Refresh Rate (Hz)", min_value=0.0, format="%.1f")
ram = st.number_input("RAM Size (GB)", min_value=0.0, format="%.1f")
battery = st.number_input("Battery Capacity (mAh)", min_value=0.0, format="%.1f")

if st.button("Predict 💰"):
    input_data = {
        "Clock_Speed_GHz": clock_speed,
        "NFC_Yes": 1 if nfc_selection == "Yes" else 0,
        "NFC_No": 1 if nfc_selection == "No" else 0,
        "rating": rating,
        "PPI": ppi,
        "fast_charging_power": fast_charging,
        "Storage Size GB": storage,
        "Refresh_Rate": refresh_rate,
        "RAM Size GB": ram,
        "battery_capacity": battery
    }

    # Convert to DataFrame
    df = pd.DataFrame([input_data])

    # Ensure correct column order
    df = df[features_list]

    # Predict
    prediction_idx = pipeline.predict(df)[0]
    prediction_label = label_encoder.inverse_transform([prediction_idx])[0]

    probability = 0.0
    if hasattr(pipeline, "predict_proba"):
        probability = pipeline.predict_proba(df)[0].max()

    st.success(f"Predicted Price Category: **{prediction_label}**")
    st.metric("Confidence", f"{probability:.2%}")

    with st.expander("🔍 Features Used"):
        st.json(input_data)