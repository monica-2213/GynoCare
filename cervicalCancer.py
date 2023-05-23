import streamlit as st

# Page title
st.title("GynoCare: Cervical Cancer Diagnosis and Recommendations")

# Introduction and explanation
st.write("Welcome to GynoCare, an expert system for cervical cancer diagnosis and treatment recommendations. Please answer the following questions to assess your risk and receive personalized recommendations.")

# Questions and user input
age = st.slider("How old are you?", min_value=18, max_value=100, step=1)
hpv_positive = st.radio("Have you ever tested positive for high-risk types of HPV?", ("Yes", "No"))
smoking_history = st.radio("Do you have a history of smoking or are you currently a smoker?", ("Yes", "No"))
immune_conditions = st.radio("Have you been diagnosed with any conditions or are you undergoing treatments that weaken your immune system?", ("Yes", "No"))
family_history = st.radio("Does anyone in your immediate family have a history of cervical cancer?", ("Yes", "No"))
abnormal_pap = st.radio("Have you ever had abnormal Pap test results in the past?", ("Yes", "No"))
sexual_behavior = st.radio("Have you engaged in high-risk sexual behavior?", ("Yes", "No"))
cin_diagnosis = st.radio("Have you ever been diagnosed with cervical intraepithelial neoplasia (CIN) or cervical dysplasia?", ("Yes", "No"))
hpv_vaccination = st.radio("Have you received the HPV vaccination?", ("Yes", "No"))
abnormal_bleeding = st.radio("Are you currently experiencing abnormal vaginal bleeding?", ("Yes", "No"))
pelvic_pain = st.radio("Are you currently experiencing pelvic pain?", ("Yes", "No"))
unusual_discharge = st.radio("Are you currently experiencing unusual discharge?", ("Yes", "No"))

# Submit button
submit = st.button("Submit")

# Logic for processing user input
if submit:
    # Perform risk assessment and provide recommendations based on the user's input
    risk_score = 0
    
    # Age-based risk assessment
    if age >= 18 and age <= 25:
        risk_score += 1
    elif age >= 26 and age <= 30:
        risk_score += 2
    elif age >= 31 and age <= 40:
        risk_score += 3
    elif age >= 41 and age <= 50:
        risk_score += 4
    elif age > 50:
        risk_score += 5
    
    # Other risk factors assessment
    if hpv_positive == "Yes":
        risk_score += 2
    
    if smoking_history == "Yes":
        risk_score += 1
    
    if immune_conditions == "Yes":
        risk_score += 2
    
    if family_history == "Yes":
        risk_score += 1
    
    if abnormal_pap == "Yes":
        risk_score += 2
    
    if sexual_behavior == "Yes":
        risk_score += 2
    
    if cin_diagnosis == "Yes":
        risk_score += 2
    
    if hpv_vaccination == "Yes":
        risk_score -= 1
    
    if abnormal_bleeding == "Yes":
        risk_score += 1
    
    if pelvic_pain == "Yes":
        risk_score += 1
    
    if unusual_discharge == "Yes":
        risk_score += 1
    
    # Example: Display the risk assessment result and recommendations
    st.subheader("Risk Assessment Result")
    if risk_score <= 5:
        st.write("Based on your answers, your risk for cervical cancer is low.")
    elif risk_score <= 10:
        st.write("Based on your answers, your risk for cervical cancer is moderate.")
    else:
        st.write("Based on your answers, your risk for cervical cancer is high.")
    
    st.subheader("Recommendations")
    if risk_score <= 5:
        st.write("Here are some general recommendations for maintaining a healthy lifestyle and preventing cervical cancer:")
        st.write("- Schedule regular Pap tests and follow your healthcare provider's recommendations.")
        st.write("- Practice safe sex and use barrier methods of contraception.")
        st.write("- Quit smoking if you are a smoker.")
    elif risk_score <= 10:
        st.write("Based on your moderate risk for cervical cancer, it is recommended to:")
        st.write("- Schedule regular Pap tests and follow your healthcare provider's recommendations.")
        st.write("- Consider discussing HPV vaccination with your healthcare provider.")
        st.write("- Practice safe sex and use barrier methods of contraception.")
        st.write("- Quit smoking if you are a smoker.")
    else:
        st.write("Based on your high risk for cervical cancer, it is strongly recommended to:")
        st.write("- Schedule regular Pap tests and follow your healthcare provider's recommendations.")
        st.write("- Discuss HPV vaccination with your healthcare provider if you haven't received it.")
        st.write("- Practice safe sex and use barrier methods of contraception.")
        st.write("- Quit smoking if you are a smoker.")
        st.write("- Consult with a healthcare professional for further evaluation and management options.")
