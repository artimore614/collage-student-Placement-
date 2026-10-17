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
    max_value=10.0,
    value=6.5,
    step=0.1
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
    max_value=10.0,
    value=7.0,
    step=0.1
)

internship = st.selectbox(
    "Internship Experience",
    ["No", "Yes"]
)

extra_curricular = st.number_input(
    "Extra Curricular Score",
    min_value=0.0,
    max_value=10.0,
    value=7.0,
    step=0.1
)

communication = st.number_input(
    "Communication Skills",
    min_value=0.0,
    max_value=10.0,
    value=7.0,
    step=0.1
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

    # Create input DataFrame using the model's expected feature names
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

    # Show probabilities using the model's actual class order
    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(new_student)[0]
        classes = list(model.classes_)

        st.write("### Prediction Probability")

        if 0 in classes:
            not_placed_prob = probabilities[classes.index(0)] * 100
            st.write(f"Not Placed: {not_placed_prob:.2f}%")

        if 1 in classes:
            placed_prob = probabilities[classes.index(1)] * 100
            st.write(f"Placed: {placed_prob:.2f}%")

    st.caption("Note: This is a model-based estimate, not a guarantee of actual placement.")
