import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load dataset
url = 'https://datahub.io/machine-learning/cervical-cancer/r/cervical-cancer_csv.csv'
df = pd.read_csv(url)

# Load trained model
model = joblib.load('cervical_cancer_model.pkl')

# Tests recommendation
tests = {
    'Pap test (Pap smear)': 'This is a routine screening test that involves collecting cells from the cervix and examining them under a microscope to look for any abnormal changes.'
}

# Food recommendation
foods = {
    'Fruits and vegetables': 'Eating a diet rich in fruits and vegetables provides essential nutrients, vitamins, and antioxidants that can help boost the immune system and protect against cancer. Dark, leafy greens, cruciferous vegetables like broccoli and cauliflower, and brightly colored fruits like berries and citrus fruits are particularly beneficial.'
}

# Helplines
helplines = {
    'National Cancer Society Malaysia (NCSM)': '1-800-88-1000'
}

def diagnose_cervical_cancer(age, num_pregnancies, smokes, horm_contra, iud, stds, first_sexual_intercourse, num_sexual_partners):
    # Perform diagnosis based on input features using a trained model
    # Return the diagnosis and risk percentage
    features = np.array([[age, num_pregnancies, smokes, horm_contra, iud, stds, first_sexual_intercourse, num_sexual_partners]])
    prediction = model.predict(features)
    probability = model.predict_proba(features)[0][1]

    if prediction == 1:
        return f'Based on your answers, your risk of cervical cancer is {probability*100:.2f}%. We recommend that you take further tests and contact helplines for support.'
    else:
        return f'Based on your answers, your risk of cervical cancer is {probability*100:.2f}%. You are at low risk of cervical cancer.'

def main():
    st.title('Cervical Cancer Diagnose and Recommendations System')
    
    # Sidebar
    st.sidebar.title('Patient Information')
    age = st.sidebar.number_input('Age', min_value=18, max_value=80, value=25, step=1)
    num_pregnancies = st.sidebar.number_input('Number of pregnancies', min_value=0, max_value=20, value=0, step=1)
    smokes = st.sidebar.selectbox('Do you smoke?', ['Yes', 'No'])
    horm_contra = st.sidebar.selectbox('Are you using hormonal contraceptives?', ['Yes', 'No'])
    iud = st.sidebar.selectbox('Are you using intrauterine device (IUD)?', ['Yes', 'No'])
    stds = st.sidebar.selectbox('Have you had any STDs?', ['Yes', 'No'])
    first_sexual_intercourse = st.sidebar.number_input('Age of first sexual intercourse', min_value=10, max_value=40, value=15, step=1)
    num_sexual_partners = st.sidebar.number_input('Number of sexual partners', min_value=0, max_value=50, value=1, step=1)
    st.sidebar.markdown('---')

    # Diagnose
    diagnose_button = st.button('Diagnose')
    if diagnose_button:
        diagnosis, risk_percentage = diagnose_cervical_cancer(age, num_pregnancies, num_sexual_partners, first_sexual_intercourse, num_smokes, hormonal_contraceptives)
    if diagnosis == 'Negative':
        st.success(f"Based on your answers, your risk of cervical cancer is {risk_percentage}. You are at low risk of cervical cancer.")
    else:
        st.error(f"Based on your answers, your risk of cervical cancer is {risk_percentage}. We recommend that you take further tests and contact helplines for support.")
    st.sidebar.markdown('---')

    # Tests recommendation
    st.header('Tests Recommendation')
    st.write('The following tests are recommended for cervical cancer screening:')
    for test, description in tests.items():
        st.write(f'- {test}: {description}')

    # Food recommendation
    st.header('Food Recommendation')
    st.write('The following foods can help prevent cervical cancer:')
    for food, description in foods.items():
        st.write(f'- {food}: {description}')

    # Helplines
    st.header('Helplines')
    st.write('The following helplines provide support for cervical cancer patients:')
    for helpline, number in helplines.items():
        st.write(f'- {helpline}: {number}')
