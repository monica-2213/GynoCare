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
        'rule1': {'Age': '<30', 'Number of sexual partners': '>2', 'First sexual intercourse': '<18', 'Num of pregnancies': '>0',
                  'Smokes': 'Yes', 'Smokes (years)': '>5', 'Hormonal Contraceptives': 'Yes', 'Hormonal Contraceptives (years)': '>5',
                  'IUD': 'No', 'STDs': 'Yes', 'STDs (number)': '>0', 'STDs:condylomatosis': 'No',
                  'STDs:cervical condylomatosis': 'No', 'STDs: Number of diagnosis': '>0',
                  'STDs: Time since first diagnosis': '>1', 'Dx:Cancer': 'Yes', 'Dx:CIN': 'Yes',
                  'Dx': 'Yes', 'Hinselmann': '1', 'Citology': '1', 'Biopsy': '1', 'Diagnosis': 'Positive'},
        'rule2': {'Age': '>=30', 'Number of sexual partners': '<=2', 'First sexual intercourse': '>=18', 'Num of pregnancies': '0',
                  'Smokes': 'No', 'Smokes (years)': '0', 'Hormonal Contraceptives': 'No', 'Hormonal Contraceptives (years)': '0',
                  'IUD': 'No', 'STDs': 'No', 'STDs (number)': '0', 'STDs:condylomatosis': 'No',
                  'STDs:cervical condylomatosis': 'No', 'STDs: Number of diagnosis': '0',
                  'STDs: Time since first diagnosis': '0', 'Dx:Cancer': 'No', 'Dx:CIN': 'No',
                  'Dx': 'No', 'Hinselmann': '0', 'Citology': '0', 'Biopsy': '0', 'Diagnosis': 'Negative'},
        # Add more rules as per your requirements
    }

    # Check the symptoms against the defined rules
    for rule, conditions in rules.items():
        match = True
        for symptom, value in conditions.items():
            if symptom not in symptoms or symptoms[symptom] != value:
                match = False
                break
        if match:
            return conditions['Diagnosis']
    
    return 'Unknown'  # Return 'Unknown' if no matching rule is found


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

    # Display the diagnosis result with different colors
    st.subheader('Diagnosis Result')
    if diagnosis == 'Positive':
        st.write('Based on your symptoms, the diagnosis suggests **positive** for cervical cancer. Please consult a healthcare professional for further evaluation.',
                 unsafe_allow_html=True)
        st.markdown('<style>div.stButton > button:first-child {background-color: red;}</style>', unsafe_allow_html=True)
    elif diagnosis == 'Negative':
        st.write('Based on your symptoms, the diagnosis suggests **negative** for cervical cancer. However, it is always advisable to consult a healthcare professional for confirmation.',
                 unsafe_allow_html=True)
        st.markdown('<style>div.stButton > button:first-child {background-color: yellow;}</style>', unsafe_allow_html=True)
    else:
        st.write('The diagnosis result is **unknown**. Please consult a healthcare professional for proper evaluation.')

if __name__ == '__main__':
    main()
