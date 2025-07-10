import streamlit as st
from health_alerts import health_recommendation
from risk_assessment import heart_risk
from health_utils import calculate_bmi

st.set_page_config(page_title="AI Health Monitoring", page_icon="🧠", layout="centered")

st.title("🧠 AI-Based Health Monitoring and Recommendation System")
st.markdown("Enter your health data to receive recommendations and risk assessment.")

age = st.number_input("Age", 0, 120, 30)
bp = st.number_input("Blood Pressure (mmHg)", 80, 250, 120)
sugar = st.number_input("Blood Sugar (mg/dL)", 50, 400, 100)
cholesterol = st.number_input("Cholesterol (mg/dL)", 100, 400, 180)
weight = st.number_input("Weight (kg)", 30, 200, 70)
height = st.number_input("Height (cm)", 100, 220, 170)
smoker = st.selectbox("Do you smoke?", ["No", "Yes"]) == "Yes"

if st.button("Analyze"):
    st.balloons()
    data = {
        'blood_pressure': bp,
        'blood_sugar': sugar,
        'cholesterol': cholesterol
    }

    st.subheader("📋 Health Recommendations:")
    recs = health_recommendation(data)
    for r in recs:
        st.write("✅", r)

    st.subheader("❤️ Heart Risk Assessment:")
    st.write(heart_risk(age, bp, cholesterol, smoker))

    st.subheader("📏 BMI Report:")
    bmi, category = calculate_bmi(weight, height)
    st.write(f"**BMI:** {bmi:.2f} – {category}")

# Optional ML Model placeholder
# from models.ml_model import predict_health_status