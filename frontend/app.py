import streamlit as st
import requests

st.set_page_config(page_title="AI MLOps Dashboard")

st.title("🤖 AI Model Dashboard")

text = st.text_area("Enter text")

if st.button("Predict"):
    res = requests.post(
        "http://localhost:8000/predict",
        json={"text": text}
    )
    st.json(res.json())