import streamlit as st
import pandas as pd

# Load the cervical cancer dataset
url = 'https://datahub.io/machine-learning/cervical-cancer/r/cervical-cancer.csv'
data = pd.read_csv(url)

# Define the rule for predicting cervical cancer risk based on age
def predict_cervical_cancer_risk(age):
    if age < 30:
        return 'Low'
    elif age < 40:
        return 'Moderate'
    else:
        return 'High'

# Define the Streamlit app
def app():
    st.title('Cervical Cancer Risk Prediction')
    st.write('Enter your age below to predict your risk of cervical cancer.')

    # Create a slider for age input
    age = st.slider('Age', 18, 100, 30)

    # Make prediction based on age input
    risk = predict_cervical_cancer_risk(age)

    # Display prediction result
    st.write('Your risk of cervical cancer is:', risk)

if __name__ == '__main__':
    app()
