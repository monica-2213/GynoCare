import streamlit as st

# Step 1: Gather user input
st.header("GynoCare - Cervical Cancer Diagnosis and Treatment Recommendations")
st.subheader("Risk Assessment")

# Create input fields for symptoms, medical history, lifestyle factors, and family history
symptoms = st.multiselect("Select Symptoms:", [
    "Abnormal vaginal bleeding or discharge",
    "Pelvic pain or discomfort",
    "Pain during sexual intercourse",
    "Unexplained weight loss",
    "Fatigue or loss of energy",
    "Changes in bowel or urinary habits",
    "Back or leg pain",
    "Swelling of the legs"
])

medical_history = st.multiselect("Medical History Factors:", [
    "Previous abnormal Pap test results",
    "Previous history of cervical dysplasia or cervical intraepithelial neoplasia (CIN)",
    "Previous treatment for cervical cancer or precancerous cervical lesions",
    "Previous exposure to diethylstilbestrol (DES) in utero",
    "Weakened immune system",
    "Long-term use of oral contraceptives"
])

lifestyle_factors = st.multiselect("Lifestyle Factors:", [
    "Human papillomavirus (HPV) infection",
    "Smoking tobacco",
    "Multiple sexual partners or early sexual activity",
    "Lack of regular cervical cancer screening"
])

family_history = st.multiselect("Family History Factors:", [
    "Family history of cervical cancer",
    "Family history of certain hereditary conditions, such as Lynch syndrome or Fanconi anemia"
])

# Step 2: Perform risk assessment and generate recommendations
if st.button("Assess Risk"):
    # Perform inference using the acquired expert knowledge and user inputs
    risk_score = 0

    # Symptoms
    if "Abnormal vaginal bleeding or discharge" in symptoms:
        risk_score += 1
    if "Pelvic pain or discomfort" in symptoms:
        risk_score += 1
    if "Pain during sexual intercourse" in symptoms:
        risk_score += 1
    if "Unexplained weight loss" in symptoms:
        risk_score += 1
    if "Fatigue or loss of energy" in symptoms:
        risk_score += 1
    if "Changes in bowel or urinary habits" in symptoms:
        risk_score += 1
    if "Back or leg pain" in symptoms:
        risk_score += 1
    if "Swelling of the legs" in symptoms:
        risk_score += 1

    # Medical history factors
    if "Previous abnormal Pap test results" in medical_history:
        risk_score += 1
    if "Previous history of cervical dysplasia or cervical intraepithelial neoplasia (CIN)" in medical_history:
        risk_score += 1
    if "Previous treatment for cervical cancer or precancerous cervical lesions" in medical_history:
        risk_score += 1
    if "Previous exposure to diethylstilbestrol (DES) in utero" in medical_history:
        risk_score += 1
    if "Weakened immune system" in medical_history:
        risk_score += 1
    if "Long-term use of oral contraceptives" in medical_history:
        risk_score += 1

    # Lifestyle factors
    if "Human papillomavirus (HPV) infection" in lifestyle_factors:
        risk_score += 1
    if "Smoking tobacco" in lifestyle_factors:
        risk_score += 1
    if "Multiple sexual partners or early sexual activity" in lifestyle_factors:
        risk_score += 1
    if "Lack of regular cervical cancer screening" in lifestyle_factors:
        risk_score += 1
        
    # Family history factors
    if "Family history of cervical cancer" in family_history:
        risk_score += 1
    if "Family history of certain hereditary conditions, such as Lynch syndrome or Fanconi anemia" in family_history:
        risk_score += 1

    # Generate recommendations based on risk score
    recommendations = []
    if risk_score >= 6:
        recommendations.append("Based on your risk assessment, it is recommended to consult with your healthcare provider for further evaluation and screening.")
    elif risk_score >= 3:
        recommendations.append("Based on your risk assessment, it is recommended to schedule a Pap test and HPV test with your healthcare provider.")
    else:
        recommendations.append("Based on your risk assessment, it is recommended to continue practicing regular cervical cancer screenings as recommended by your healthcare provider.")

# Display the results
st.subheader("Risk Assessment Results")
st.write("Risk Score:", risk_score)

st.subheader("Recommendations")
for recommendation in recommendations:
    st.write("- " + recommendation)
    
if __name__ == "__main__":
    st.set_page_config(page_title="GynoCare", page_icon=":female-doctor:")
    st.sidebar.title("GynoCare")
    st.sidebar.write("Welcome to GynoCare")
    st.sidebar.write("Please provide the requested information and click 'Assess Risk' to get personalized recommendations.")
    st.sidebar.write("For further assistance, please contact your healthcare provider.")
    st.sidebar.write("© 2023 GynoCare")
