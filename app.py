import streamlit as st
import pickle
import numpy as np

# Load model
with open("gs_log_reg_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Heart Disease Prediction App 💓")
st.write("Fill in the patient details below:")

# Age
age = st.number_input("Age (in years)", min_value=18, max_value=100, value=45)

# Sex
sex = st.radio("Sex", options=["Male", "Female"])
sex_val = 1 if sex == "Male" else 0

# Chest Pain Type
cp_options = {
    "Typical angina (related to heart)": 0,
    "Atypical angina (not related to heart)": 1,
    "Non-anginal pain (e.g. esophageal spasms)": 2,
    "Asymptomatic": 3
}
cp = st.selectbox("Chest Pain Type", options=list(cp_options.keys()))
cp_val = cp_options[cp]

# Resting BP
trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=80, max_value=200, value=120)

# Cholesterol
chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=100, max_value=600, value=200,
                       help="Above 200 mg/dl is considered high.")

# Fasting Blood Sugar
fbs = st.radio("Fasting Blood Sugar > 120 mg/dl", options=["Yes", "No"])
fbs_val = 1 if fbs == "Yes" else 0

# Resting ECG
restecg_options = {
    "Normal": 0,
    "ST-T wave abnormality": 1,
    "Left ventricular hypertrophy": 2
}
restecg = st.selectbox("Resting ECG Results", options=list(restecg_options.keys()))
restecg_val = restecg_options[restecg]

# Max Heart Rate Achieved
thalach = st.number_input("Maximum Heart Rate Achieved", min_value=60, max_value=220, value=150)

# Exercise Induced Angina
exang = st.radio("Exercise Induced Angina", options=["Yes", "No"])
exang_val = 1 if exang == "Yes" else 0

# Oldpeak
oldpeak = st.slider("ST Depression Induced by Exercise (Oldpeak)", 0.0, 6.0, 1.0, step=0.1,
                    help="Higher values indicate more stress on the heart.")

# Slope
slope_options = {
    "Upsloping (better heart rate with exercise)": 0,
    "Flat (typical healthy response)": 1,
    "Downsloping (unhealthy heart sign)": 2
}
slope = st.selectbox("Slope of ST Segment", options=list(slope_options.keys()))
slope_val = slope_options[slope]

# Number of major vessels
ca = st.selectbox("Number of Major Vessels Colored by Fluoroscopy (0-3)", options=[0, 1, 2, 3])

# Thalassemia
thal_options = {
    "Normal": 1,
    "Fixed Defect (old heart damage)": 3,
    "Reversible Defect (blood flow issue under stress)": 7
}
thal = st.selectbox("Thalassemia Test Result", options=list(thal_options.keys()))
thal_val = thal_options[thal]

# Prepare input for prediction
input_data = np.array([[age, sex_val, cp_val, trestbps, chol, fbs_val,
                        restecg_val, thalach, exang_val, oldpeak,
                        slope_val, ca, thal_val]])

# Predict button
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("⚠️ The model predicts that the person is likely to have heart disease.")
    else:
        st.success("✅ The model predicts that the person is unlikely to have heart disease.")
