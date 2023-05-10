import pandas as pd
import streamlit as st

st.title("Cervical Cancer Risk Calculator")

age = st.number_input("Age in years", min_value=1, max_value=100)
num_sexual_partners = st.number_input("Number of sexual partners", min_value=0, max_value=20)
first_sexual_intercourse = st.number_input("Age at first sexual intercourse", min_value=1, max_value=100)
num_pregnancies = st.number_input("Number of pregnancies", min_value=0, max_value=20)
smoking = st.radio("Do you smoke?", options=["Yes", "No"])
if smoking == "Yes":
    smoking_years = st.number_input("Number of years smoked", min_value=1, max_value=50)
else:
    smoking_years = 0
hormonal_contraceptives = st.radio("Do you use hormonal contraceptives?", options=["Yes", "No"])
if hormonal_contraceptives == "Yes":
    hormonal_contraceptives_years = st.number_input("Number of years using hormonal contraceptives", min_value=1, max_value=50)
else:
    hormonal_contraceptives_years = 0
iud = st.radio("Do you use an intrauterine device (IUD)?", options=["Yes", "No"])
if iud == "Yes":
    iud_years = st.number_input("Number of years with an IUD", min_value=1, max_value=50)
else:
    iud_years = 0
std = st.radio("Have you ever had a sexually transmitted disease (STD)?", options=["Yes", "No"])
if std == "Yes":
    num_std_diagnoses = st.number_input("Number of STD diagnoses", min_value=1, max_value=10)
    time_since_first_std = st.number_input("Time since first STD diagnosis (years)", min_value=1, max_value=50)
    time_since_last_std = st.number_input("Time since lastif submit:
    risk = cervical_cancer_rules(age, num_sexual_partners, first_sexual_intercourse, num_pregnancies, smoking, smoking_years, hormonal_contraceptives, hormonal_contraceptives_years, iud, iud_years, std, num_std_diagnoses, time_since_first_std, time_since_last_std)
    st.write(f"Your estimated risk of cervical cancer is {risk}%") STD diagnosis (years)", min_value=1, max_value=50)
else:
    num_std_diagnoses = 0
    time_since_first_std = 0
    time_since_last_std = 0

submit = st.button("Submit")

if submit:
    risk = cervical_cancer_rules(age, num_sexual_partners, first_sexual_intercourse, num_pregnancies, smoking, smoking_years, hormonal_contraceptives, hormonal_contraceptives_years, iud, iud_years, std, num_std_diagnoses, time_since_first_std, time_since_last_std)
    st.write(f"Your estimated risk of cervical cancer is {risk}%")
                                      
if __name__ == "__main__":
    main()
