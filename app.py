import streamlit as st
import pickle
import pandas as pd

# Load the trained model
with open("student_performance_model.pkl", "rb") as file:
    model = pickle.load(file)

# Page title
st.title("Student Performance Predictor")

st.write(
    "Enter the student's study hours, attendance, and previous marks "
    "to predict their final marks."
)

# User inputs
study_hours = st.number_input(
    "Study Hours",
    min_value=0.0,
    max_value=24.0,
    value=6.0
)

attendance = st.number_input(
    "Attendance (%)",
    min_value=0.0,
    max_value=100.0,
    value=85.0
)

previous_marks = st.number_input(
    "Previous Marks",
    min_value=0.0,
    max_value=100.0,
    value=70.0
)

# Prediction button
if st.button("Predict Final Marks"):

    new_student = pd.DataFrame({
        "Study_Hours": [study_hours],
        "Attendance": [attendance],
        "Previous_Marks": [previous_marks]
    })

    prediction = model.predict(new_student)

    st.success(f"Predicted Final Marks: {prediction[0]:.2f}")
