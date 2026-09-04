import streamlit as st
import pandas as pd
import joblib

# Page configuration
st.set_page_config(
    page_title="Student Placement Prediction",
    page_icon="🎓",
    layout="centered"
)

# Load trained model
model = joblib.load("placement_model.pkl")

# Title
st.title("🎓 Smart Student Placement Prediction System")
st.write("Enter the student's details to predict placement status.")

st.divider()

# Input fields
iq = st.number_input(
    "IQ",
    min_value=0,
    max_value=200,
    value=100
)

prev_sem_result = st.number_input(
    "Previous Semester Result",
    min_value=0.0,
    max_value=100.0,
    value=70.0
)

cgpa = st.number_input(
    "CGPA",
    min_value=0.0,
    max_value=10.0,
    value=7.0,
    step=0.1
)

academic_performance = st.number_input(
    "Academic Performance",
    min_value=0.0,
    max_value=100.0,
    value=70.0
)

internship = st.selectbox(
    "Internship Experience",
    ["No", "Yes"]
)

extra_curricular = st.number_input(
    "Extra Curricular Score",
    min_value=0.0,
    max_value=100.0,
    value=50.0
)

communication = st.number_input(
    "Communication Skills",
    min_value=0.0,
    max_value=10.0,
    value=7.0
)

projects = st.number_input(
    "Projects Completed",
    min_value=0,
    max_value=20,
    value=2
)

# Convert Internship to 0/1
internship_value = 1 if internship == "Yes" else 0

# Prediction button
if st.button("🔮 Predict Placement"):

    # Create input DataFrame
    new_student = pd.DataFrame({
        "IQ": [iq],
        "Prev_Sem_Result": [prev_sem_result],
        "CGPA": [cgpa],
        "Academic_Performance": [academic_performance],
        "Internship_Experience": [internship_value],
        "Extra_Curricular_Score": [extra_curricular],
        "Communication_Skills": [communication],
        "Projects_Completed": [projects]
    })

    # Prediction
    prediction = model.predict(new_student)[0]

    # Show result
    st.divider()

    if prediction == 1:
        st.success("🎉 Prediction: Student is likely to be PLACED!")
    else:
        st.error("❌ Prediction: Student is likely to be NOT PLACED.")

    # Show probability
    if hasattr(model, "predict_proba"):
        probability = model.predict_proba(new_student)[0]

        st.write("### Prediction Probability")

        st.write(
            f"Not Placed: {probability[0] * 100:.2f}%"
        )

        st.write(
            f"Placed: {probability[1] * 100:.2f}%"
        )