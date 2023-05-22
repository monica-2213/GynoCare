import streamlit as st

# Function to evaluate rules and provide recommendations
def evaluate_rules(symptoms, history, age, lifestyle):
    recommendations = []
    
    if "Positive HPV test" in symptoms:
        recommendations.append("Recommend colposcopy and biopsy for further evaluation.")
    
    if "Abnormal Pap test" in symptoms:
        recommendations.append("Recommend colposcopy and biopsy for further evaluation.")
    
    if history.get("Family history of cervical cancer") == "Yes":
        recommendations.append("Recommend more frequent Pap tests or HPV testing.")
    
    if history.get("Previous abnormal Pap test") == "Yes":
        recommendations.append("Recommend more frequent Pap tests or colposcopy examinations.")
    
    if history.get("HPV infection duration") >= 12:
        recommendations.append("Recommend colposcopy and consider treatment options such as cryotherapy, LEEP, or cone biopsy.")
    
    if history.get("Diagnosis") == "Cervical cancer":
        recommendations.append("Recommend surgery, radiation therapy, chemotherapy, or a combination of treatments based on the stage and specific characteristics of the cancer.")
    
    if lifestyle.get("Smoking status") == "Smoker":
        recommendations.append("Provide information and resources for smoking cessation programs.")
    
    if lifestyle.get("Sexually active") == "Yes":
        recommendations.append("Provide information on safe sex practices and discuss the benefits of the HPV vaccine.")
    
    if age >= 21:
        recommendations.append("Recommend regular Pap tests or HPV testing based on age and guidelines.")
    
    if history.get("Weakened immune system") == "Yes":
        recommendations.append("Recommend more frequent Pap tests or colposcopy examinations and consider treatment options based on the individual's condition.")
    
    if history.get("History of CIN") == "Yes":
        recommendations.append("Recommend regular Pap tests or colposcopy examinations to monitor for recurrence or progression.")
    
    if symptoms.count("Abnormal vaginal bleeding") > 0 or symptoms.count("Pelvic pain") > 0 or symptoms.count("Discomfort during sex") > 0:
        recommendations.append("Recommend immediate medical evaluation to assess the cause of the symptoms.")
    
    if history.get("Hysterectomy") == "Yes":
        recommendations.append("Evaluate the reason for the hysterectomy and recommend screening based on the presence or absence of residual cervical tissue.")
    
    if lifestyle.get("Multiple sexual partners") == "Yes" or lifestyle.get("High-risk sexual behaviors") == "Yes":
        recommendations.append("Recommend regular Pap tests or HPV testing and provide information on safe sex practices and the prevention of sexually transmitted infections.")
    
    return recommendations

# Function to get risk level based on recommendations
def get_risk_level(recommendations):
    if len(recommendations) >= 3:
        return "High"
    elif len(recommendations) >= 1:
        return "Moderate"
    else:
        return "Low"

# Streamlit app
def main():
    st.title("GynoCare - Cervical Cancer Expert System")
    
    # User input
    st.header("Patient Information")
    symptoms = st.multiselect("Select symptoms:", ["Positive HPV test", "Abnormal Pap test", "Abnormal vaginal bleeding", "Pelvic pain", "Discomfort during sex"])
    history = {
        "Family history of cervical cancer": st.radio("Family history of cervical cancer:", ("Yes", "No")),
        "Previous abnormal Pap test": st.radio("Previous abnormal Pap test:", ("Yes", "No")),
        "HPV infection duration": st.number_input("HPV infection duration (months):", min_value=0),
        "Diagnosis": st.radio("Diagnosis:", ("Cervical cancer", "No diagnosis")),
        "Weakened immune system": st.radio("Weakened immune system:", ("Yes", "No")),
        "History of CIN": st.radio("History of CIN:", ("Yes", "No")),
        "Hysterectomy": st.radio("Hysterectomy:", ("Yes", "No"))
    }
    age = st.slider("Age:", min_value=18, max_value=100)
    lifestyle = {
        "Smoking status": st.radio("Smoking status:", ("Smoker", "Non-smoker")),
        "Sexually active": st.radio("Sexually active:", ("Yes", "No")),
        "Multiple sexual partners": st.radio("Multiple sexual partners:", ("Yes", "No")),
        "High-risk sexual behaviors": st.radio("High-risk sexual behaviors:", ("Yes", "No"))
    }
    
    # Diagnose button
    if st.button("Diagnose"):
        # Evaluate rules and get recommendations
        recommendations = evaluate_rules(symptoms, history, age, lifestyle)
        
        # Determine risk level
        risk_level = get_risk_level(recommendations)
        
        # Display recommendations with risk level colors
        st.header("Recommendations")
        if recommendations:
            for idx, recommendation in enumerate(recommendations):
                if risk_level == "High":
                    st.markdown(f"<span style='color:red;'>{idx+1}. {recommendation}</span>", unsafe_allow_html=True)
                elif risk_level == "Moderate":
                    st.markdown(f"<span style='color:orange;'>{idx+1}. {recommendation}</span>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<span style='color:green;'>{idx+1}. {recommendation}</span>", unsafe_allow_html=True)
        else:
            st.write("No recommendations at this time.")
    
    
if __name__ == "__main__":
    main()
