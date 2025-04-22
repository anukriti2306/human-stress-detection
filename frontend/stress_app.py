import streamlit as st
import requests

#Flask API Endpoint
API_URL = "http://127.0.0.1:5000/predict"

#Streamlit app title
st.title("🛏️HUMAN STRESS DETECTOR USING SLEEP DATA FROM SaYoPillow🛏️")
st.subheader("Enter in your sleep data below:")

#collected all the inputs from the user

snoring_rate=st.number_input("Snoring rate", min_value=0.0, max_value=100.0, step=0.1)
respiration_rate=st.number_input("Respiration rate", min_value=0.0, max_value=100.0, step=0.1)
body_temperature=st.number_input("Body temperature(Celsius)", min_value=20.0, max_value=45.0, step=0.1)
limb_movement = st.number_input("Limb Movement", min_value=0.0, max_value=100.0, step=0.1)
blood_oxygen = st.number_input("Blood Oxygen (%)", min_value=50.0, max_value=100.0, step=0.1)
eye_movement = st.number_input("Eye Movement", min_value=0.0, max_value=100.0, step=0.1)
sleeping_hours = st.number_input("Sleeping Hours", min_value=0.0, max_value=24.0, step=0.1)
heart_rate = st.number_input("Heart Rate", min_value=30.0, max_value=200.0, step=1.0)


if st.button("Predict Stress Level"):
    #build the data payload for the API
    payload={
        "snoring rate":snoring_rate,
        "respiration rate":respiration_rate,
        "body temperature":body_temperature,
        "limb movement":limb_movement,
        "blood oxygen":blood_oxygen,
        "eye movement": eye_movement,
        "sleeping hours":sleeping_hours,
        "heart rate":heart_rate
    }

    #only select the features the model needs
    filtered_payload={
         "limb_movement": limb_movement,
        "sleeping_hours": sleeping_hours,
        "snoring_rate": snoring_rate,
        "eye_movement": eye_movement,
        "body_temperature": body_temperature
    }

    #Call the Flask API
    try:
        response=requests.post(API_URL, json=filtered_payload)
        result=response.json()

        #display the prediction
        st.success(f"✅ Predicted Stress Level: {result['description']} (Level {result['stress_level']})")

    except Exception as e:
        st.error("Could not connect to the prediction server")
        st.error(f"Details:{e}")