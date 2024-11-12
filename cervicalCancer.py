import streamlit as st

# Page configuration for title and layout
st.set_page_config(page_title="GynoCare: Cervical Cancer Diagnosis", layout="wide")

# Custom styling
st.markdown(
    """
    <style>
        body {
            background-color: #f4f7fc;
        }
        .title {
            color: #4CAF50;
            font-size: 36px;
            font-weight: bold;
        }
        .header {
            color: #3E8E41;
            font-size: 24px;
            font-weight: bold;
        }
        .subheader {
            color: #3E8E41;
            font-size: 18px;
            font-weight: semi-bold;
        }
        .container {
            background-color: #ffffff;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        .button {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
            padding: 10px 20px;
            border-radius: 5px;
        }
        .button:hover {
            background-color: #45a049;
        }
        .section-title {
            color: #3E8E41;
            font-size: 22px;
            font-weight: bold;
        }
        .recommendation {
            background-color: #e0f7fa;
            padding: 15px;
            border-radius: 10px;
            color: #00695c;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Page title
st.markdown('<div class="title">GynoCare: Cervical Cancer Diagnosis and Recommendations</div>', unsafe_allow_html=True)

# Introduction and explanation
st.write("Welcome to GynoCare, an expert system for cervical cancer diagnosis and treatment recommendations. Please answer the following questions to assess your risk and receive personalized recommendations.")

# Create containers for each section
with st.container():
    st.markdown('<div class="section-title">Please answer the following questions</div>', unsafe_allow_html=True)

    # Questions and user input
    age = st.slider("How old are you?", min_value=18, max_value=100, step=1, key="age")
    hpv_positive = st.radio("Have you ever tested positive for high-risk types of HPV?", ("Yes", "No"), key="hpv_positive")
    smoking_history = st.radio("Do you have a history of smoking or are you currently a smoker?", ("Yes", "No"), key="smoking_history")
    immune_conditions = st.radio("Have you been diagnosed with any conditions or are you undergoing treatments that weaken your immune system?", ("Yes", "No"), key="immune_conditions")
    family_history = st.radio("Does anyone in your immediate family have a history of cervical cancer?", ("Yes", "No"), key="family_history")
    abnormal_pap = st.radio("Have you ever had abnormal Pap test results in the past?", ("Yes", "No"), key="abnormal_pap")
    sexual_behavior = st.radio("Have you engaged in high-risk sexual behavior?", ("Yes", "No"), key="sexual_behavior")
    cin_diagnosis = st.radio("Have you ever been diagnosed with cervical intraepithelial neoplasia (CIN) or cervical dysplasia?", ("Yes", "No"), key="cin_diagnosis")
    hpv_vaccination = st.radio("Have you received the HPV vaccination?", ("Yes", "No"), key="hpv_vaccination")
    abnormal_bleeding = st.radio("Are you currently experiencing abnormal vaginal bleeding?", ("Yes", "No"), key="abnormal_bleeding")
    pelvic_pain = st.radio("Are you currently experiencing pelvic pain?", ("Yes", "No"), key="pelvic_pain")
    unusual_discharge = st.radio("Are you currently experiencing unusual discharge?", ("Yes", "No"), key="unusual_discharge")

# Submit button with custom styling
submit = st.button("Submit", key="submit", use_container_width=True)

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
    
    # Display the risk assessment result and recommendations
    st.markdown('<div class="header">Risk Assessment Result</div>', unsafe_allow_html=True)
    if risk_score <= 5:
        st.write("Based on your answers, your risk for cervical cancer is low.")
    elif risk_score <= 10:
        st.write("Based on your answers, your risk for cervical cancer is moderate.")
    else:
        st.write("Based on your answers, your risk for cervical cancer is high.")
    
    st.markdown('<div class="header">Recommendations</div>', unsafe_allow_html=True)
    if risk_score <= 5:
        st.markdown('<div class="recommendation">Here are some general recommendations for maintaining a healthy lifestyle and preventing cervical cancer:</div>', unsafe_allow_html=True)
        st.write("- Schedule regular Pap tests and follow your healthcare provider's recommendations.")
        st.write("- Practice safe sex and use barrier methods of contraception.")
        st.write("- Quit smoking if you are a smoker.")
    elif risk_score <= 10:
        st.markdown('<div class="recommendation">Based on your moderate risk for cervical cancer, it is recommended to:</div>', unsafe_allow_html=True)
        st.write("- Schedule regular Pap tests and follow your healthcare provider's recommendations.")
        st.write("- Consider discussing HPV vaccination with your healthcare provider.")
        st.write("- Practice safe sex and use barrier methods of contraception.")
        st.write("- Quit smoking if you are a smoker.")
    else:
        st.markdown('<div class="recommendation">Based on your high risk for cervical cancer, it is strongly recommended to:</div>', unsafe_allow_html=True)
        st.write("- Schedule regular Pap tests and follow your healthcare provider's recommendations.")
        st.write("- Discuss HPV vaccination with your healthcare provider if you haven't received it.")
        st.write("- Practice safe sex and use barrier methods of contraception.")
        st.write("- Quit smoking if you are a smoker.")
        st.write("- Consult with a healthcare professional for further evaluation and management options.")
