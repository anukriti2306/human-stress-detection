import streamlit as st
import requests

# Flask API Endpoint
API_URL = "http://127.0.0.1:5000/predict"

# Streamlit app title
st.title("🛏️ HUMAN STRESS DETECTOR USING SLEEP DATA FROM SaYoPillow")
st.subheader("Enter your key sleep data below:")

# Only the important model features
snoring_rate = st.number_input("Snoring Rate", min_value=0.0, max_value=100.0, step=0.1)
eye_movement = st.number_input("Eye Movement", min_value=0.0, max_value=100.0, step=0.1)
body_temperature = st.number_input("Body Temperature (°C)", min_value=20.0, max_value=45.0, step=0.1)
limb_movement = st.number_input("Limb Movement", min_value=0.0, max_value=100.0, step=0.1)
sleeping_hours = st.number_input("Sleeping Hours", min_value=0.0, max_value=24.0, step=0.1)

if st.button("Predict Stress Level"):
    # Data payload for the API with only necessary features
    payload = {
        "snoring_rate": snoring_rate,
        "eye_movement": eye_movement,
        "body_temperature": body_temperature,
        "limb_movement": limb_movement,
        "sleeping_hours": sleeping_hours
    }

    try:
        response = requests.post(API_URL, json=payload)
        result = response.json()

        # Display the prediction
        st.success(f"✅ Predicted Stress Level: {result['description']} (Level {result['stress_level']})")

    except Exception as e:
        st.error("❌ Could not connect to the prediction server.")
        st.error(f"Details: {e}")
