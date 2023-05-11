import streamlit as st
import pandas as pd

# Load the cervical cancer dataset
df = pd.read_csv('https://datahub.io/machine-learning/cervical-cancer/r/cervical-cancer.csv')

# Define the rules for the diagnostic system
def diagnose_cervical_cancer(age, number_of_sexual_partners, first_sexual_intercourse, num_pregnancies, 
                             stds_num, stds_condylomatosis, stds_cervical_condylomatosis, stds_vaginal_condylomatosis, 
                             stds_vulvo_perineal_condylomatosis, stds_syphilis, stds_pelvic_inflammatory_disease,
                             stds_genital_herpes, stds_molluscum_contagiosum, stds_aids, stds_hiv):
    
    if age < 21:
        return "Not at risk for cervical cancer"
    
    if (age >= 21 and number_of_sexual_partners >= 5) or (age >= 21 and stds_num >= 2):
        return "High risk for cervical cancer"
    
    if first_sexual_intercourse < 16 or num_pregnancies >= 3:
        return "Moderate risk for cervical cancer"
    
    if (age >= 21 and stds_condylomatosis == 1) or (age >= 21 and stds_cervical_condylomatosis == 1) or \
       (age >= 21 and stds_vaginal_condylomatosis == 1) or (age >= 21 and stds_vulvo_perineal_condylomatosis == 1) or \
       (age >= 21 and stds_syphilis == 1) or (age >= 21 and stds_pelvic_inflammatory_disease == 1) or \
       (age >= 21 and stds_genital_herpes == 1) or (age >= 21 and stds_molluscum_contagiosum == 1) or \
       (age >= 21 and stds_aids == 1) or (age >= 21 and stds_hiv == 1):
        return "Moderate risk for cervical cancer"
    
    return "Low risk for cervical cancer"

# Define the Streamlit app
def app():
    # Set the app title
    st.title("Cervical Cancer Diagnostic System")
    
    # Create the user input form
    age = st.slider("Age", 15, 84)
    number_of_sexual_partners = st.slider("Number of sexual partners", 0, 28)
    first_sexual_intercourse = st.slider("Age at first sexual intercourse", 10, 32)
    num_pregnancies = st.slider("Number of pregnancies", 0, 11)
    stds_num = st.slider("Number of sexually transmitted diseases (STDs)", 0, 7)
    stds_condylomatosis = st.selectbox("Presence of genital warts (condylomatosis)", ["No", "Yes"])
    stds_cervical_condylomatosis = st.selectbox("Presence of cervical warts (condylomatosis)", ["No", "Yes"])
    stds_vaginal_condylomatosis = st.selectbox("Presence of vaginal warts (condylomatosis)", ["No", "Yes"])
    stds_vulvo_perineal_condylomatosis = st.selectbox("Presence of vulvo-perineal warts (condylomatosis)", ["No", "Yes"])
    stds_syphilis = st.selectbox("Presence of syphilis", ["No", "Yes"])
    stds_pelvic_inflammatory_disease = st.selectbox("Presence of pelvic inflammatory disease", ["No", "Yes"])
    stds_genital_herpes = st.selectbox("Presence of genital herpes", ["No", "Yes"])
    stds_molluscum_contagiosum = st.selectbox("Presence of molluscum contagiosum", ["No", "Yes"])
    stds_aids = st.selectbox("Presence of AIDS", ["No", "Yes"])
    stds_hiv = st.selectbox("Presence of HIV", ["No", "Yes"])
    
    # Add a submit button
    if st.button("Diagnose"):
        # Diagnose cervical cancer based on user input
        diagnosis = diagnose_cervical_cancer(age, number_of_sexual_partners, first_sexual_intercourse, num_pregnancies, 
                                             stds_num, stds_condylomatosis, stds_cervical_condylomatosis, 
                                             stds_vaginal_condylomatosis, stds_vulvo_perineal_condylomatosis, 
                                             stds_syphilis, stds_pelvic_inflammatory_disease, stds_genital_herpes, 
                                             stds_molluscum_contagiosum, stds_aids, stds_hiv)
        
        # Display the diagnosis to the user
        st.write("Based on your input, you are at:", diagnosis, "risk for cervical cancer.")

    
if __name__ == '__main__':
    app()
