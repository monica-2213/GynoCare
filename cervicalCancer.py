import streamlit as st
import pandas as pd

# Load the cervical cancer dataset
@st.cache
def load_dataset():
    st.text('Loading dataset...')
    df = pd.read_csv('https://datahub.io/machine-learning/cervical-cancer/r/cervical-cancer.csv')
    st.success('Dataset loaded successfully!')
    return df

df = load_dataset()

def cervical_cancer_diagnosis(symptoms):
    # Define the rules for cervical cancer diagnosis
    rules = {
        'rule1': {'Bleeding': '1', 'Smoking': '1', 'Hormonal Contraceptives': '1', 'Diagnosis': 'Positive'},
        'rule2': {'Bleeding': '0', 'Smoking': '0', 'Hormonal Contraceptives': '0', 'Diagnosis': 'Negative'},
        # Add more rules as per your requirements
    }

    # Check the symptoms against the defined rules
    for rule, conditions in rules.items():
        match = True
        for symptom, value in conditions.items():
            if symptoms[symptom] != value:
                match = False
                break
        if match:
            return conditions['Diagnosis']
    
    return 'Unknown'  # Return 'Unknown' if no matching rule is found

# Define the interrelated questions for the questionnaire
questions = {
    'Bleeding': 'Have you experienced any abnormal vaginal bleeding?',
    'Smoking': 'Do you smoke?',
    'Hormonal Contraceptives': 'Have you used hormonal contraceptives?',
    # Add more questions as per your requirements
}

# Main Streamlit code
def main():
    st.title('Cervical Cancer Diagnosis')
    st.write('Answer a few questions to get your diagnosis.')

    # Initialize the dictionary to store user input
    symptoms = {}

    # Display the questionnaire and capture user input
    for key, question in questions.items():
        answer = st.radio(question, ('Yes', 'No'))
        symptoms[key] = '1' if answer == 'Yes' else '0'
        st.write('---')

    # Perform the diagnosis
    diagnosis = cervical_cancer_diagnosis(symptoms)

    # Display the diagnosis result
    st.subheader('Diagnosis Result')
    if diagnosis == 'Positive':
        st.write('Based on your symptoms, the diagnosis suggests **positive** for cervical cancer. Please consult a healthcare professional for further evaluation.')
    elif diagnosis == 'Negative':
        st.write('Based on your symptoms, the diagnosis suggests **negative** for cervical cancer. However, it is always advisable to consult a healthcare professional for confirmation.')
    else:
        st.write('The diagnosis result is **unknown**. Please consult a healthcare professional for proper evaluation.')

if __name__ == '__main__':
    main()
