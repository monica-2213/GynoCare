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


# Define the interrelated questions for the questionnaire
questions = {
    'Age': 'What is your age?',
    'Number of sexual partners': 'How many sexual partners have you had?',
    'First sexual intercourse': 'At what age did you have your first sexual intercourse?',
    'Num of pregnancies': 'How many pregnancies have you had?',
    'Smokes': 'Do you smoke?',
    'Smokes (years)': 'For how many years have you been smoking?',
    'Hormonal Contraceptives': 'Have you used hormonal contraceptives?',
    'Hormonal Contraceptives (years)': 'For how many years have you used hormonal contraceptives?',
    'IUD': 'Have you used an intrauterine device (IUD)?',
    'STDs': 'Have you had any sexually transmitted diseases (STDs)?',
    'STDs (number)': 'How many STDs have you had?',
    'STDs:condylomatosis': 'Have you had condylomatosis (genital warts)?',
    'STDs:cervical condylomatosis': 'Have you had cervical condylomatosis?',
    'STDs: Number of diagnosis': 'How many times have you been diagnosed with an STD?',
    'STDs: Time since first diagnosis': 'How long has it been since your first STD diagnosis?',
    'Dx:Cancer': 'Have you been diagnosed with cervical cancer?',
    'Dx:CIN': 'Have you been diagnosed with cervical intraepithelial neoplasia (CIN)?',
    'Dx': 'Have you been diagnosed with any other disease?',
    'Hinselmann': 'Have you been diagnosed with Hinselmann?',
    'Citology': 'Have you had a cytology test?',
    'Biopsy': 'Have you had a biopsy?',
    }

#Main Streamlit code
def main():
    st.title('Cervical Cancer Diagnosis')
    st.write('Answer a few questions to get your diagnosis.')
    
    # Initialize the dictionary to store user input
    symptoms = {}

    # Display the questionnaire and capture user input
    for key, question in questions.items():
        if key == 'Number of sexual partners':
            sexual_partners = st.selectbox(question, ('None/0', '1', '2', '3', '4', '5+'))
            if sexual_partners != 'None/0':
                symptoms[key] = sexual_partners
                st.write('---')
                first_sexual_intercourse = st.number_input('At what age did you have your first sexual intercourse?', min_value=0, step=1)
                symptoms['First sexual intercourse'] = str(first_sexual_intercourse)
        elif key == 'Smokes':
            smoking = st.radio(question, ('No', 'Yes'))
            if smoking == 'Yes':
                symptoms[key] = 'Yes'
                st.write('---')
                smoking_years = st.number_input('For how many years have you been smoking?', min_value=0, step=1)
                symptoms['Smokes (years)'] = str(smoking_years)
        elif key == 'Hormonal Contraceptives':
            contraceptives = st.radio(question, ('No', 'Yes'))
            if contraceptives == 'Yes':
                symptoms[key] = 'Yes'
                st.write('---')
                contraceptive_years = st.number_input('For how many years have you used hormonal contraceptives?', min_value=0, step=1)
                symptoms['Hormonal Contraceptives (years)'] = str(contraceptive_years)
        elif key == 'STDs':
            stds = st.radio(question, ('No', 'Yes'))
            if stds == 'Yes':
                symptoms[key] = 'Yes'
                st.write('---')
                num_stds = st.number_input('How many STDs have you had?', min_value=0, step=1)
                symptoms['STDs (number)'] = str(num_stds)
                st.write('---')
                num_diagnosis = st.number_input('How many times have you been diagnosed with an STD?', min_value=0, step=1)
                symptoms['STDs: Number of diagnosis'] = str(num_diagnosis)
                st.write('---')
                time_since_diagnosis = st.number_input('How long has it been since your first STD diagnosis?', min_value=0, step=1)
                symptoms['STDs: Time since first diagnosis'] = str(time_since_diagnosis)
        else:
            options = ('No', 'Yes')
            answer = st.selectbox(question, options)
            symptoms[key] = 'Yes' if answer == 'Yes' else 'No'
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
