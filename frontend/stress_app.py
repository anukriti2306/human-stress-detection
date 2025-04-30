import streamlit as st
import requests

# Flask API Endpoint
API_URL = "http://127.0.0.1:5000/predict"

# --- Page Configuration ---
st.set_page_config(page_title="Stress Detector", layout="centered")

# --- Custom Simple CSS Styling (Instagram-inspired) ---
st.markdown("""
    <style>
    body {
        background-color: #F0F2F5;
        font-family: 'Helvetica', sans-serif;
        color: #262626;
    }

    .stApp {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 2rem;
        max-width: 600px;
        margin: auto;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }

    h1, h2 {
        color: #333;
        text-align: center;
    }

    .stTitle {
        font-size: 32px;
        font-weight: bold;
        color: #333;
    }

    .stSubheader {
        font-size: 18px;
        color: #555;
        text-align: center;
    }

    input, .stNumberInput>div>div>input {
        background-color: #fafafa;
        border-radius: 8px;
        border: 1px solid #dbdbdb;
        padding: 0.8rem;
        margin-bottom: 1rem;
        font-size: 16px;
    }

    .stButton>button {
        background-color: #0095f6;
        color: white;
        border-radius: 8px;
        padding: 1rem;
        width: 100%;
        border: none;
        font-size: 16px;
        cursor: pointer;
    }

    .stButton>button:hover {
        background-color: #007bb5;
    }

    .stSuccess {
        background-color: #28a745;
        color: white;
        padding: 1rem;
        border-radius: 8px;
        font-weight: bold;
        text-align: center;
    }

    .stError {
        background-color: #e74c3c;
        color: white;
        padding: 1rem;
        border-radius: 8px;
        font-weight: bold;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# --- Streamlit App Title ---
st.title("Human Stress Detector")
st.subheader("Based on Sleep Data from SaYoPillow")

# --- Input Fields ---
snoring_rate = st.number_input("Snoring Rate", min_value=0.0, max_value=100.0, step=0.1)
eye_movement = st.number_input("Eye Movement", min_value=0.0, max_value=100.0, step=0.1)
body_temperature = st.number_input("Body Temperature (°C)", min_value=20.0, max_value=45.0, step=0.1)
limb_movement = st.number_input("Limb Movement", min_value=0.0, max_value=100.0, step=0.1)
sleeping_hours = st.number_input("Sleeping Hours", min_value=0.0, max_value=24.0, step=0.1)

# --- Button to trigger prediction ---
if st.button("Predict Stress Level"):
    # Data payload for the API
    payload = {
        "snoring_rate": snoring_rate,
        "eye_movement": eye_movement,
        "body_temperature": body_temperature,
        "limb_movement": limb_movement,
        "sleeping_hours": sleeping_hours
    }

    try:
        # Send the data to the prediction API
        response = requests.post(API_URL, json=payload)
        result = response.json()

        # Display prediction result
        st.success(f"Predicted Stress Level: {result['description']} (Level {result['stress_level']})")

    except Exception as e:
        # Error handling
        st.error("Could not connect to the prediction server.")
        st.error(f"Details: {e}")
