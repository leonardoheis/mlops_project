import streamlit as st
import requests
import json

st.title("Model Prediction")

with st.form("prediction_form"):
    model_name = st.text_input("Model Name", value="my_model")
    
    st.subheader("Features (JSON)")
    features_input = st.text_area("Enter features as JSON", value='{"feature1": 0.5, "feature2": 1.2}')
    
    submitted = st.form_submit_button("Predict")
    
    if submitted:
        try:
            features = json.loads(features_input)
            payload = {
                "model_name": model_name,
                "features": features
            }
            
            response = requests.post("http://localhost:8000/api/v1/predict", json=payload)
            if response.status_code == 200:
                st.success("Prediction Successful")
                st.json(response.json())
            else:
                st.error(f"Error: {response.text}")
        except json.JSONDecodeError:
            st.error("Invalid JSON format for features")
        except Exception as e:
            st.error(f"Failed to connect: {e}")
