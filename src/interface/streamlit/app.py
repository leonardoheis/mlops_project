import streamlit as st
import requests

st.set_page_config(page_title="MLOps Dashboard", layout="wide")

st.title("MLOps Project Dashboard")

st.markdown("""
Welcome to the MLOps Project Dashboard. Use the sidebar to navigate between:
- **Training**: Trigger model training.
- **Prediction**: Make predictions with trained models.
- **Monitoring**: View model performance and drift reports.
""")

# Check API health
try:
    response = requests.get("http://localhost:8000/health")
    if response.status_code == 200:
        st.success("API is Online")
    else:
        st.error("API is Offline")
except:
    st.error("Could not connect to API")
