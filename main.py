import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import joblib

# Load dataset
data = pd.read_csv("heart_disease_dataset.csv")

# Features & Target
X = data.drop(columns=['heart_disease'])
y = data['heart_disease']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_scaled, y_train)

# Save scaler and model
joblib.dump(scaler, "scaler.pkl")
joblib.dump(model, "heart_model.pkl")

# Streamlit UI
st.title("❤️ Heart Disease Prediction App")

st.write("Enter patient details to predict the risk of heart disease:")

# Input fields
age = st.number_input("Age", 18, 100, 40)
sex = st.selectbox("Sex (1 = Male, 0 = Female)", [0, 1])
cp = st.selectbox("Chest Pain Type (1-4)", [1, 2, 3, 4])
trestbps = st.number_input("Resting Blood Pressure", 80, 200, 120)
chol = st.number_input("Cholesterol Level", 100, 600, 200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (1 = True, 0 = False)", [0, 1])
restecg = st.selectbox("Rest ECG (0-2)", [0, 1, 2])
thalach = st.number_input("Max Heart Rate Achieved", 60, 220, 150)
exang = st.selectbox("Exercise Induced Angina (1 = Yes, 0 = No)", [0, 1])
oldpeak = st.number_input("ST Depression", 0.0, 10.0, 1.0, step=0.1)
slope = st.selectbox("Slope (1-3)", [1, 2, 3])
ca = st.selectbox("Number of Major Vessels (0-4)", [0, 1, 2, 3, 4])
thal = st.selectbox("Thal (3 = Normal, 6 = Fixed Defect, 7 = Reversible Defect)", [3, 6, 7])
smoking = st.selectbox("Smoking (1 = Yes, 0 = No)", [0, 1])
diabetes = st.selectbox("Diabetes (1 = Yes, 0 = No)", [0, 1])
bmi = st.number_input("BMI", 10.0, 50.0, 25.0, step=0.1)

# Predict button
if st.button("Predict"):
    # Load model & scaler
    scaler = joblib.load("scaler.pkl")
    model = joblib.load("heart_model.pkl")

    # Prepare input
    input_data = pd.DataFrame([[age, sex, cp, trestbps, chol, fbs, restecg, thalach,
                                exang, oldpeak, slope, ca, thal, smoking, diabetes, bmi]],
                                columns=X.columns)

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Prediction
    prediction = model.predict(input_scaled)[0]

    if prediction == 1:
        st.error("🚨 The patient is likely to have Heart Disease.")
    else:
        st.success("✅ The patient is unlikely to have Heart Disease.")
