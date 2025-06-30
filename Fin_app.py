
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
model = joblib.load("xgb_model.pkl")

st.title("Financial Inclusion Prediction App")

st.write("Enter details to predict whether the person is likely to have a bank account.")

# User input fields
year = st.selectbox("Year", [2016, 2017, 2018])
location_type = st.selectbox("Location Type", ["Urban", "Rural"])
cellphone_access = st.selectbox("Cellphone Access", ["Yes", "No"])
household_size = st.number_input("Household Size", min_value=1, max_value=20, value=3)
age_of_respondent = st.number_input("Age", min_value=10, max_value=100, value=30)
gender = st.selectbox("Gender", ["Male", "Female"])
country = st.selectbox("Country", ["Kenya", "Rwanda", "Tanzania", "Uganda"])
relationship = st.selectbox("Relationship with Head", [
    "Head of Household", "Spouse", "Parent", "Other relative", 
    "Other non-relatives"])
marital_status = st.selectbox("Marital Status", [
    "Married/Living together", "Single/Never Married", "Widowed", "Dont know"])
education_level = st.selectbox("Education Level", [
    "Primary education", "Secondary education", "Tertiary education", 
    "Vocational/Specialised training", "Other/Dont know/RTA"])
job_type = st.selectbox("Job Type", [
    "Farming and Fishing", "Formally employed Government", "Formally employed Private",
    "Government Dependent", "Informally employed", "No Income", "Other Income",
    "Remittance Dependent", "Self employed"])

# Predict button
if st.button("Validate"):
    # Base input dictionary
    data = {
        'year': year,
        'location_type': 1 if location_type == "Urban" else 0,
        'cellphone_access': 1 if cellphone_access == "Yes" else 0,
        'household_size': household_size,
        'age_of_respondent': age_of_respondent,
        'gender_of_respondent': 1 if gender == "Male" else 0,
        'country_Rwanda': 1 if country == "Rwanda" else 0,
        'country_Tanzania': 1 if country == "Tanzania" else 0,
        'country_Uganda': 1 if country == "Uganda" else 0,
        'relationship_with_head_Head of Household': 1 if relationship == "Head of Household" else 0,
        'relationship_with_head_Other non-relatives': 1 if relationship == "Other non-relatives" else 0,
        'relationship_with_head_Other relative': 1 if relationship == "Other relative" else 0,
        'relationship_with_head_Parent': 1 if relationship == "Parent" else 0,
        'relationship_with_head_Spouse': 1 if relationship == "Spouse" else 0,
        'marital_status_Dont know': 1 if marital_status == "Dont know" else 0,
        'marital_status_Married/Living together': 1 if marital_status == "Married/Living together" else 0,
        'marital_status_Single/Never Married': 1 if marital_status == "Single/Never Married" else 0,
        'marital_status_Widowed': 1 if marital_status == "Widowed" else 0,
        'education_level_Other/Dont know/RTA': 1 if education_level == "Other/Dont know/RTA" else 0,
        'education_level_Primary education': 1 if education_level == "Primary education" else 0,
        'education_level_Secondary education': 1 if education_level == "Secondary education" else 0,
        'education_level_Tertiary education': 1 if education_level == "Tertiary education" else 0,
        'education_level_Vocational/Specialised training': 1 if education_level == "Vocational/Specialised training" else 0,
        'job_type_Farming and Fishing': 1 if job_type == "Farming and Fishing" else 0,
        'job_type_Formally employed Government': 1 if job_type == "Formally employed Government" else 0,
        'job_type_Formally employed Private': 1 if job_type == "Formally employed Private" else 0,
        'job_type_Government Dependent': 1 if job_type == "Government Dependent" else 0,
        'job_type_Informally employed': 1 if job_type == "Informally employed" else 0,
        'job_type_No Income': 1 if job_type == "No Income" else 0,
        'job_type_Other Income': 1 if job_type == "Other Income" else 0,
        'job_type_Remittance Dependent': 1 if job_type == "Remittance Dependent" else 0,
        'job_type_Self employed': 1 if job_type == "Self employed" else 0,
    }

    input_df = pd.DataFrame([data])
    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.success("✅ Likely to Own a Bank Account")
    else:
        st.warning("❌ Unlikely to Own a Bank Account")
