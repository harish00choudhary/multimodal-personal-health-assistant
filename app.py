import streamlit as st
import joblib
from src.text_analyzer import analyze_text

label_map = joblib.load("label_map.pkl")

# Load model & vectorizer
model = joblib.load("disease_model.pkl") # src - ?

vectorizer = joblib.load("vectorizer.pkl")

st.set_page_config(page_title="Multimodal Health Assistant", layout="centered")

st.title("🩺 Multimodal Personal Health Assistant")
st.write("⚠️ This tool is for educational purposes only. Not a medical diagnosis.")

# Text input
user_input = st.text_area(
    "Describe your symptoms in natural language:",
    placeholder="I am feeling dizzy, weak and sweating a lot..."
)

if st.button("Analyze Symptoms"):
    if user_input.strip() == "":
        st.warning("Please enter symptoms.")
    else:
        pred_label, confidence = analyze_text(
            user_input, model, vectorizer
        )

        pred_disease = label_map.get(pred_label, "Unknown condition")

        st.success(f"🧠 Predicted Condition: **{pred_disease}**")
        st.info(f"📊 Confidence: **{confidence:.2f}%**")
