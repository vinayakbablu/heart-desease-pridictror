
# <h1>❤️ Heart Disease Predictor</h1>

This project is a **Machine Learning-based web application** that predicts whether a person is likely to have **heart disease** based on health parameters such as age, cholesterol, blood pressure, smoking habits, diabetes status, and more.

The project uses **Logistic Regression** as the baseline model, with options to extend to **Random Forest** and **XGBoost** for improved performance. The web interface is built using **Streamlit**.

---

## 📌 Features

* Cleaned and preprocessed dataset of heart patients.
* Logistic Regression model trained on health indicators.
* User-friendly **Streamlit web app** where users can input parameters to get predictions.
* Evaluation metrics: Accuracy, Precision, Recall, F1-score, and Confusion Matrix.

---

## 🗂 Dataset

The dataset contains patient health records with the following features:

* **age** → Age of the patient
* **sex** → 1 = Male, 0 = Female
* **cp** → Chest pain type (1–4)
* **trestbps** → Resting blood pressure
* **chol** → Serum cholesterol level
* **fbs** → Fasting blood sugar (>120 mg/dl, 1 = True, 0 = False)
* **restecg** → Resting ECG results
* **thalach** → Maximum heart rate achieved
* **exang** → Exercise induced angina (1 = Yes, 0 = No)
* **oldpeak** → ST depression induced by exercise
* **slope** → Slope of peak exercise ST segment
* **ca** → Number of major vessels (0–4)
* **thal** → Thalassemia status (3, 6, 7)
* **smoking** → Smoking habit (1 = Yes, 0 = No)
* **diabetes** → Diabetes (1 = Yes, 0 = No)
* **bmi** → Body Mass Index
* **heart\_disease** → Target variable (1 = Disease, 0 = No disease)

---

## ⚙️ Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/heart-disease-predictor.git
   cd heart-disease-predictor
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the environment:

   * **Windows**:

     ```bash
     venv\Scripts\activate
     ```
   * **Mac/Linux**:

     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Running the Project

Run the **Streamlit web app**:

```bash
streamlit run app.py
```

Then open the link (default: `http://localhost:8501`) in your browser.

