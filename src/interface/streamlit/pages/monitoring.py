import streamlit as st
import streamlit.components.v1 as components
import requests

st.title("Model Monitoring")

if st.button("Refresh Report"):
    try:
        response = requests.get("http://localhost:8000/api/v1/reports")
        if response.status_code == 200:
            components.html(response.text, height=800, scrolling=True)
        else:
            st.error("Could not fetch report")
    except Exception as e:
        st.error(f"Failed to connect: {e}")
