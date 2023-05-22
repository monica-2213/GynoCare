import streamlit as st

# Rule definitions and recommendations
RULES = {
    "Positive HPV test": "Recommend colposcopy and biopsy for further evaluation.",
    "Abnormal Pap test": "Recommend colposcopy and biopsy for further evaluation.",
    "Family history of cervical cancer": "Recommend more frequent Pap tests or HPV testing.",
    "Previous abnormal Pap test": "Recommend more frequent Pap tests or colposcopy examinations.",
    "HPV infection duration": "Recommend colposcopy and consider treatment options such as cryotherapy, LEEP, or cone biopsy.",
    "Diagnosis": "Recommend surgery, radiation therapy, chemotherapy, or a combination of treatments based on the stage and specific characteristics of the cancer.",
    "Smoking status": "Provide information and resources for smoking cessation programs.",
    "Sexually active": "Provide information on safe sex practices and discuss the benefits of the HPV vaccine.",
    "Weakened immune system": "Recommend more frequent Pap tests or colposcopy examinations and consider treatment options based on the individual's condition.",
    "History of CIN": "Recommend regular Pap tests or colposcopy examinations to monitor for recurrence or progression.",
    "Abnormal vaginal bleeding": "Recommend immediate medical evaluation to assess the cause of the symptoms.",
    "Pelvic pain": "Recommend immediate medical evaluation to assess the cause of the symptoms.",
    "Discomfort during sex": "Recommend immediate medical evaluation to assess the cause of the symptoms.",
    "Hysterectomy": "Evaluate the reason for the hysterectomy and recommend screening based on the presence or absence of residual cervical tissue.",
    "Multiple sexual partners": "Recommend regular Pap tests or HPV testing and provide information on safe sex practices and the prevention of sexually transmitted infections.",
    "High-risk sexual behaviors": "Recommend regular Pap tests or HPV testing and provide information on safe sex practices and the prevention of sexually transmitted infections."
}

# Function to evaluate rules and provide recommendations
def evaluate_rules(symptoms, history, lifestyle):
    recommendations = []
    for symptom in symptoms:
        if symptom in RULES:
            recommendations.append(RULES[symptom])
    for key, value in history.items():
        if key in RULES and value == "Yes":
            recommendations.append(RULES[key])
    for key, value in lifestyle.items():
        if key in RULES and value == "Yes":
            recommendations.append(RULES[key])
    return recommendations

# Function to determine risk level
def get_risk_level(recommendations):
    if len(recommendations) >= 3:
        return "High"
    elif len(recommendations) >= 1:
        return "Moderate"
    else:
        return "Low"

# Function to calculate risk percentage
def calculate_risk_percentage(risk_level):
    if risk_level == "High":
        return 80
    elif risk_level == "Moderate":
        return 50
    else:
        return 20

# Streamlit app
def main():
    st.title("GynoCare - Cervical Cancer Expert System")
    
    # User input
    st.header("Patient Information")
    age = st.slider("Age:", min_value=18, max_value=100)
    symptoms = st.multiselect("Select symptoms:", list(RULES.keys()))
    history = {}
    lifestyle = {}
    for key in RULES.keys():
        if key.startswith("Family history") or key.startswith("Previous abnormal") or key == "HPV infection duration":
            history[key] = st.radio(key, ("Yes", "No"))
        else:
            lifestyle[key] = st.radio(key, ("Yes", "No"))
    
    # Diagnose button
    if st.button("Diagnose"):
        # Evaluate rules and get recommendations
        recommendations = evaluate_rules(symptoms, history, lifestyle)
        
        # Determine risk level
        risk_level = get_risk_level(recommendations)
        
        # Calculate risk percentage
        risk_percentage = calculate_risk_percentage(risk_level)
        
        # Display risk level and percentage
        st.header("Cervical Cancer Diagnosis Result")
        if risk_level == "High":
            st.markdown("<span style='color:red;'>High Risk</span>", unsafe_allow_html=True)
        elif risk_level == "Moderate":
            st.markdown("<span style='color:orange;'>Moderate Risk</span>", unsafe_allow_html=True)
        else:
            st.markdown("<span style='color:green;'>Low Risk</span>", unsafe_allow_html=True)
        st.write(f"Risk Percentage: {risk_percentage}%")
        
        # Display recommendations with risk level colors
        st.header("Recommendations")
        if recommendations:
            for idx, recommendation in enumerate(recommendations):
                risk_color = "red" if risk_level == "High" else "orange" if risk_level == "Moderate" else "green"
                st.markdown(f"<span style='color:{risk_color};'>{idx+1}. {recommendation}</span>", unsafe_allow_html=True)
        else:
            st.write("No recommendations at this time.")

if __name__ == "__main__":
    main()
