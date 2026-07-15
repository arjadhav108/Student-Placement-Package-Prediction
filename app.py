import streamlit as st
import pandas as pd
import pickle

# Load trained pipeline
pipe = pickle.load(open("placement_pipe.pkl", "rb"))

st.set_page_config(page_title="Student Placement Package Prediction")

st.title("🎓 Student Placement Package Prediction")
st.write("Enter student details to predict the expected salary package.")

# -----------------------
# User Inputs
# -----------------------

gender = st.selectbox("Gender", ["M", "F"])

ssc_p = st.number_input("SSC Percentage", 0.0, 100.0, 70.0)

hsc_p = st.number_input("HSC Percentage", 0.0, 100.0, 70.0)

hsc_s = st.selectbox(
    "HSC Stream",
    ["Science", "Commerce", "Arts"]
)

degree_p = st.number_input("Degree Percentage", 0.0, 100.0, 70.0)

degree_t = st.selectbox(
    "Degree Type",
    ["Sci&Tech", "Comm&Mgmt", "Others"]
)

workex = st.selectbox(
    "Work Experience",
    ["Yes", "No"]
)

specialisation = st.selectbox(
    "MBA Specialisation",
    ["Mkt&Fin", "Mkt&HR"]
)

mba_p = st.number_input("MBA Percentage", 0.0, 100.0, 70.0)

status = st.selectbox(
    "Placement Status",
    ["Placed", "Not Placed"]
)

# -----------------------
# Prediction
# -----------------------

if st.button("Predict Salary"):

    input_df = pd.DataFrame(
        [[
            gender,
            ssc_p,
            hsc_p,
            hsc_s,
            degree_p,
            degree_t,
            workex,
            specialisation,
            mba_p,
            status
        ]],
        columns=[
            "gender",
            "ssc_p",
            "hsc_p",
            "hsc_s",
            "degree_p",
            "degree_t",
            "workex",
            "specialisation",
            "mba_p",
            "status"
        ]
    )

    prediction = pipe.predict(input_df)[0]

    st.success(f"Predicted Salary Package: ₹ {prediction:,.2f}")