import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_csv('https://datahub.io/machine-learning/cervical-cancer/r/cervical-cancer.csv')

# Define the rules for cervical cancer diagnosis
rules = {
    'Rule 1': {
        'conditions': [
            ('Hinselmann', '==', 1),
            ('Schiller', '==', 1),
            ('Citology', '==', 1)
        ],
        'diagnosis': 'High risk of cervical cancer'
    },
    'Rule 2': {
        'conditions': [
            ('Hinselmann', '==', 0),
            ('Schiller', '==', 1),
            ('Citology', '==', 1)
        ],
        'diagnosis': 'Moderate risk of cervical cancer'
    },
    'Rule 3': {
        'conditions': [
            ('Hinselmann', '==', 1),
            ('Schiller', '==', 0),
            ('Citology', '==', 1)
        ],
        'diagnosis': 'Moderate risk of cervical cancer'
    },
    'Rule 4': {
        'conditions': [
            ('Hinselmann', '==', 0),
            ('Schiller', '==', 0),
            ('Citology', '==', 1)
        ],
        'diagnosis': 'Low risk of cervical cancer'
    },
    'Rule 5': {
        'conditions': [
            ('Hinselmann', '==', 1),
            ('Schiller', '==', 1),
            ('Citology', '==', 0)
        ],
        'diagnosis': 'Moderate risk of cervical cancer'
    },
    'Rule 6': {
        'conditions': [
            ('Hinselmann', '==', 0),
            ('Schiller', '==', 1),
            ('Citology', '==', 0)
        ],
        'diagnosis': 'Low risk of cervical cancer'
    },
    'Rule 7': {
        'conditions': [
            ('Hinselmann', '==', 1),
            ('Schiller', '==', 0),
            ('Citology', '==', 0)
        ],
        'diagnosis': 'Low risk of cervical cancer'
    },
    'Rule 8': {
        'conditions': [
            ('Hinselmann', '==', 0),
            ('Schiller', '==', 0),
            ('Citology', '==', 0)
        ],
        'diagnosis': 'No risk of cervical cancer'
    },
}

# Streamlit app
def main():
    st.title('Cervical Cancer Expert System')
    st.write('This expert system predicts the risk of cervical cancer based on certain conditions.')

    # Display the dataset
    st.subheader('Cervical Cancer Dataset')
    st.write(df)

    # Get input from the user
    st.subheader('Diagnosis')
    hinselmann = st.selectbox('Hinselmann Test Result', [0, 1])
    schiller = st.selectbox('Schiller Test Result', [0, 1])
    citology = st.selectbox('Citology Test Result', [0, 1])

    # Check the diagnosis based on the rules
    diagnosis = check_diagnosis(hinselmann, schiller, citology)

    # Display the diagnosis
    st.subheader('Expert System Diagnosis')
    st.write(diagnosis)
    
def check_diagnosis(hinselmann, schiller, citology):
    for rule_name, rule in rules.items():
        conditions = rule['conditions']
    if all(eval(f'{condition[0]} {condition[1]} {condition[2]}') for condition in conditions):
        return rule['diagnosis']
    return 'No diagnosis available'

if __name__ == __'main'__:
    main()
