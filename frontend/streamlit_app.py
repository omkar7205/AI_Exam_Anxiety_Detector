import streamlit as st
import requests

st.title("AI-Based Exam Anxiety Detection System")

st.write("Enter your thoughts about your upcoming exams")

user_text = st.text_area("Your Text")

if st.button("Analyze Anxiety"):

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json={"text": user_text}
    )

    result = response.json()

    if result["prediction"] == "Anxiety Detected":
        st.error(f"⚠ {result['prediction']}")
    else:
        st.success(f"✅ {result['prediction']}")

    st.write(f"Confidence: {result['confidence']}%")