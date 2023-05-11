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
    
    st.write("Do you have any of the following STDs?")
    
    stds_condylomatosis = st.selectbox("Genital warts (condylomatosis)", ["No", "Yes"])
    if stds_condylomatosis == "Yes":
        stds_cervical_condylomatosis = st.selectbox("Cervical warts (condylomatosis)", ["No", "Yes"])
        stds_vaginal_condylomatosis = st.selectbox("Vaginal warts (condylomatosis)", ["No", "Yes"])
        stds_vaginalis = st.selectbox("Vaginalis", ["No", "Yes"])
    if stds_vaginalis == "Yes":
        stds_vaginal_cervicitis = st.selectbox("Vaginal cervicitis", ["No", "Yes"])
        stds_vulvodynia = st.selectbox("Vulvodynia", ["No", "Yes"])

    stds_pelvic = st.selectbox("Pelvic inflammatory disease (PID)", ["No", "Yes"])
    stds_genital_herpes = st.selectbox("Genital herpes", ["No", "Yes"])

    submit_button = st.button('Submit')

    # Create a dictionary of the user inputs
    user_inputs = {
        "Age": age,
        "Number of sexual partners": number_of_sexual_partners,
        "Age at first sexual intercourse": first_sexual_intercourse,
        "Number of pregnancies": num_pregnancies,
        "Number of sexually transmitted diseases (STDs)": stds_num,
        "Genital warts (condylomatosis)": stds_condylomatosis,
        "Cervical warts (condylomatosis)": stds_cervical_condylomatosis if stds_condylomatosis == "Yes" else None,
        "Vaginal warts (condylomatosis)": stds_vaginal_condylomatosis if stds_condylomatosis == "Yes" else None,
        "Vaginalis": stds_vaginalis,
        "Vaginal cervicitis": stds_vaginal_cervicitis if stds_vaginalis == "Yes" else None,
        "Vulvodynia": stds_vulvodynia if stds_vaginalis == "Yes" else None,
        "Pelvic inflammatory disease (PID)": stds_pelvic,
        "Genital herpes": stds_genital_herpes
    }

    # When the user clicks the submit button
    if submit_button:
        # Run the diagnosis function and pass in the user inputs
        diagnosis = diagnose_cervical_cancer(user_inputs)

        # Display the diagnosis
        st.write(f"Based on the information you have provided, your diagnosis is: {diagnosis}")

if __name__ == '__main__':
    app()
