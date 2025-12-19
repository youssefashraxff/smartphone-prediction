from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib
import pandas as pd

# Load trained objects
artifacts = joblib.load("phonePred.pkl")
pipeline = artifacts["pipeline"]
label_encoder = artifacts["label_encoder"]
features_list = artifacts["features"]

app = FastAPI(title="Smartphone Price Prediction API")

# Input schema
class PhoneRequest(BaseModel):
    Clock_Speed_GHz: float
    NFC_Yes: int
    NFC_No: int
    rating: float
    PPI: float
    fast_charging_power: float
    Storage_Size_GB: float = Field(alias="Storage Size GB")
    Refresh_Rate: float
    RAM_Size_GB: float = Field(alias="RAM Size GB")
    battery_capacity: float

@app.post("/predict")
def predict_price(data: PhoneRequest):
    # Convert input to DataFrame
    input_data = data.dict(by_alias=True)
    df = pd.DataFrame([input_data])
    
    # Ensure columns are in the correct order
    df = df[features_list]

    # Predict
    prediction_idx = pipeline.predict(df)[0]
    prediction_label = label_encoder.inverse_transform([prediction_idx])[0]
    
    # Probability
    probability = 0.0
    if hasattr(pipeline, "predict_proba"):
        probability = pipeline.predict_proba(df)[0].max()

    return {
        "price_category": prediction_label,
        "probability": float(probability),
        "features_used": input_data,
    }
