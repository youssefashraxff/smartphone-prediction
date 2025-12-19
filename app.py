import requests
import streamlit as st

st.title("Smartphone Price Prediction")

# 🏆 Selected Features: ['Clock_Speed_GHz', 'NFC_Yes', 'NFC_No', 'rating', 'PPI', 'fast_charging_power', 'Storage Size GB', 'Refresh_Rate', 'RAM Size GB', 'battery_capacity']

clock_speed = st.number_input("Clock Speed (GHz)", min_value=0.0, format="%.2f", value=None, placeholder="e.g. 2.4")
nfc_selection = st.radio("NFC Support", ["Yes", "No"])
rating = st.number_input("Rating", min_value=0.0, max_value=100.0, format="%.1f", value=None, placeholder="e.g. 80.0")
ppi = st.number_input("PPI", min_value=0.0, format="%.2f", value=None, placeholder="e.g. 400.0")
fast_charging = st.number_input("Fast Charging Power (W)", min_value=0.0, format="%.1f", value=None, placeholder="e.g. 33.0")
storage = st.number_input("Storage Size (GB)", min_value=0.0, format="%.1f", value=None, placeholder="e.g. 128.0")
refresh_rate = st.number_input("Refresh Rate (Hz)", min_value=0.0, format="%.1f", value=None, placeholder="e.g. 90.0")
ram = st.number_input("RAM Size (GB)", min_value=0.0, format="%.1f", value=None, placeholder="e.g. 8.0")
battery = st.number_input("Battery Capacity (mAh)", min_value=0.0, format="%.1f", value=None, placeholder="e.g. 5000.0")

data = {
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

if st.button("Predict"):
    if None in data.values():
        st.warning("Please fill in all numeric fields.")
    else:
        response = requests.post("http://127.0.0.1:8000/predict", json=data)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted Price Category: {result['price_category']}")
            st.metric("Probability", f"{result['probability']:.2%}")
            with st.expander("Input Features"):
                st.json(result['features_used'])
        else:
            st.error("Prediction failed")
            st.write(response.text)