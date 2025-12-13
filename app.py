import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("model/model.pkl", "rb"))

st.title("🏠 House Price Prediction")

area = st.number_input("Area (sq ft)", min_value=500)
bedrooms = st.number_input("Bedrooms", min_value=1)
bathrooms = st.number_input("Bathrooms", min_value=1)

if st.button("Predict"):
    prediction = model.predict([[area, bedrooms, bathrooms]])
    st.success(f"Estimated Price: ₹ {prediction[0]:,.2f}")
