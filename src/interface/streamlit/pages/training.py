import streamlit as st
import requests

st.title("Model Training")

with st.form("training_form"):
    model_name = st.text_input("Model Name", value="my_model")
    data_source = st.text_input("Data Source (Path)", value="data/train.csv")
    
    st.subheader("Hyperparameters")
    c_param = st.number_input("C (Inverse Regularization)", value=1.0)
    max_iter = st.number_input("Max Iterations", value=100)
    
    submitted = st.form_submit_button("Start Training")
    
    if submitted:
        payload = {
            "model_name": model_name,
            "data_source": data_source,
            "params": {
                "C": c_param,
                "max_iter": int(max_iter)
            }
        }
        
        try:
            response = requests.post("http://localhost:8000/api/v1/train", json=payload)
            if response.status_code == 200:
                st.success(f"Training started! Job ID: {response.json()['job_id']}")
                st.json(response.json())
            else:
                st.error(f"Error: {response.text}")
        except Exception as e:
            st.error(f"Failed to connect: {e}")
