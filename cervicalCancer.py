import streamlit as st

# Rule definitions and recommendations
RULES = {
    "Positive HPV test": "Recommend colposcopy and biopsy for further evaluation.",
    "Abnormal Pap test": "Recommend colposcopy and biopsy for further evaluation.",
    # Add more rules and recommendations as needed
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
    
    # Symptoms
    st.header("Symptoms")
    symptoms = []
    for symptom in RULES.keys():
        symptom_option = st.checkbox(symptom)
        if symptom_option:
            symptoms.append(symptom)
    
    # History
    st.header("History")
    history = {}
    for key in RULES.keys():
        if key.startswith("Family history") or key.startswith("Previous abnormal") or key == "HPV infection duration":
            history[key] = st.radio(key, ("Yes", "No"))
    
    # Lifestyle
    st.header("Lifestyle")
    lifestyle = {}
    for key in RULES.keys():
        if key not in history:
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
