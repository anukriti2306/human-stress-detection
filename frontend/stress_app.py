import streamlit as st
import requests

# Flask API Endpoint
API_URL = "http://127.0.0.1:5000/predict"

# --- Page Configuration ---
st.set_page_config(page_title="Stress Detector", layout="centered")

# --- Custom CSS Styling ---
st.markdown("""
    <style>
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
    </style>
""", unsafe_allow_html=True)

# --- Streamlit App Title ---
st.title("Human Stress Detector")
st.subheader("Based on Sleep Data")

# --- Input Fields ---
snoring_rate = st.number_input("Snoring Rate", min_value=0.0, max_value=100.0, step=0.1)
body_temperature = st.number_input("Body Temperature (°C)", min_value=20.0, max_value=45.0, step=0.1)
sleeping_hours = st.number_input("Sleeping Hours", min_value=0.0, max_value=24.0, step=0.1)
heart_rate = st.number_input("Heart Rate", min_value=30.0, max_value=200.0, step=1.0)

# --- Predict Button ---
if st.button("Predict Stress Level"):
    payload = {
        "heart_rate": heart_rate,
        "sleeping_hours": sleeping_hours,
        "snoring_rate": snoring_rate,
        "body_temperature": body_temperature
    }

    try:
        response = requests.post(API_URL, json=payload)
        result = response.json()

        if 'error' in result:
            st.error(f"Error: {result['error']}")
        else:
            st.success(f"Predicted Stress Level: {result['description']} (Level {result['stress_level']})")

    except Exception as e:
        st.error("Could not connect to the prediction server.")
        st.error(f"Details: {e}")
