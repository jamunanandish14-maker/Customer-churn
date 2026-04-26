import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("Customer Churn Prediction")

# ---- USER INPUTS ----

credit_score = st.number_input("Credit Score", 300, 900)
age = st.number_input("Age", 18, 100)
tenure = st.number_input("Tenure (Years)", 0, 10)
balance = st.number_input("Balance")
num_products = st.number_input("Number of Products", 1, 4)
has_card = st.selectbox("Has Credit Card", ["No", "Yes"])
is_active = st.selectbox("Is Active Member", ["No", "Yes"])
salary = st.number_input("Estimated Salary")

# Convert categorical
has_card = 1 if has_card == "Yes" else 0
is_active = 1 if is_active == "Yes" else 0

# ---- PREDICTION ----

if st.button("Predict"):
    input_data = np.array([[credit_score, age, tenure, balance,
                            num_products, has_card, is_active, salary]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ Customer is likely to leave")
    else:
        st.success("✅ Customer will stay")









class DummyModel:
    def predict(self, X):
        # simple fake logic for demo
        return [1 if X[0][0] > 500 else 0]

model = DummyModel()
