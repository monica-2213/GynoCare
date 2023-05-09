import streamlit as st
import pandas as pd

# Load dataset
url = 'https://datahub.io/machine-learning/cervical-cancer/r/cervical-cancer_csv.csv'
df = pd.read_csv(url)

# Tests recommendation
tests = {
    'Pap test (Pap smear)': 'This is a routine screening test that involves collecting cells from the cervix and examining them under a microscope to look for any abnormal changes.',
    'Human papillomavirus (HPV) test': 'This test looks for the presence of HPV, a sexually transmitted virus that can cause cervical cancer. The test may be done alone or in combination with a Pap test.',
    'Visual inspection with acetic acid (VIA)': 'This is a low-cost, simple test that involves applying a solution of acetic acid to the cervix and looking for any white areas that may indicate abnormal changes.',
    'Colposcopy': 'This is a procedure that uses a special magnifying device called a colposcope to examine the cervix for abnormal changes. If any abnormal areas are found, a biopsy may be taken for further testing.',
    'Endocervical curettage (ECC)': 'This procedure involves scraping cells from the inside of the cervix to look for abnormal changes that may not be visible during a Pap test or colposcopy.'
}

# Food recommendation
foods = {
    'Fruits and vegetables': 'Eating a diet rich in fruits and vegetables provides essential nutrients, vitamins, and antioxidants that can help boost the immune system and protect against cancer. Dark, leafy greens, cruciferous vegetables like broccoli and cauliflower, and brightly colored fruits like berries and citrus fruits are particularly beneficial.',
    'Whole grains': 'Whole grains like brown rice, quinoa, and whole wheat provide fiber, vitamins, and minerals that can help support overall health and reduce the risk of cancer.',
    'Lean proteins': 'Choosing lean protein sources like fish, chicken, and beans over processed or red meats can help reduce the risk of cancer and other health problems.',
    'Foods rich in folate': 'Folate is an essential nutrient that is important for DNA repair and cell division. Foods rich in folate include leafy greens, lentils, beans, and citrus fruits.',
    'Foods rich in vitamin C': 'Vitamin C is an antioxidant that can help protect against cancer. Foods rich in vitamin C include citrus fruits, strawberries, kiwi, and bell peppers.'
}

# Helplines
helplines = {
    'National Cancer Society Malaysia (NCSM)': '1-800-88-1000',
    'Pink Ribbon Wellness Foundation': '03-7932 4744',
    'Malaysian Ministry of Health': '03-8883 4420',
    'Cancer Research Malaysia': '03-7846 5432',
    'Hospis Malaysia': '03-9133 3936'
}

def diagnose_cervical_cancer(age, num_pregnancies, num_sexual_partners, first_sexual_intercourse, num_smokes, hormonal_contraceptives):
    # Perform diagnosis based on input features using a trained model
    # Return the diagnosis and risk percentage
    return 'Negative', '5%'

def main():
    st.title('Cervical Cancer Diagnose and Recommendations System')
    
    # Sidebar
    st.sidebar.title('Patient Information')
    age = st.sidebar.number_input('Age', min_value=18, max_value=80, value=25, step=1)
    num_pregnancies = st.sidebar.number_input('Number of pregnancies', min_value=0, max_value=20, value=0, step=1)
    smokes = st.sidebar.selectbox('Do you smoke?', ['Yes', 'No'])
    horm_contra = st.sidebar.selectbox('Are you using hormonal contraceptives?', ['Yes', 'No'])
    iud = st.sidebar.selectbox('Are you using intrauterine device (IUD)?', ['Yes', 'No'])
    stds = st.sidebar.selectbox('Have you had any STDs?', ['Yes', 'No'])
    first_sexual_intercourse = st.sidebar.number_input('Age of first sexual intercourse', min_value=10, max_value=40, value=15, step=1)
    num_sexual_partners = st.sidebar.number_input('Number of sexual partners', min_value=0, max_value=50, value=1, step=1)
    st.sidebar.markdown('---')

    # Diagnose
    diagnose_button = st.button('Diagnose')
    if diagnose_button:
        features = np.array([[age, num_pregnancies, smokes, horm_contra, iud, stds, first_sexual_intercourse, num_sexual_partners]])
        prediction = model.predict(features)
        probability = model.predict_proba(features)[0][1]

        if prediction == 1:
            st.error(f'Based on your answers, your risk of cervical cancer is {probability*100:.2f}%. We recommend that you take further tests and contact helplines for support.')
        else:
            st.success(f'Based on your answers, your risk of cervical cancer is {probability*100:.2f}%. You are at low risk of cervical cancer.')

    # Tests recommendation
    st.header('Tests Recommendation')
    st.write('The following tests are recommended for cervical cancer screening:')
    st.write('- Pap test (also known as Pap smear)')
    st.write('- Human papillomavirus (HPV) test')
    st.write('- Visual inspection with acetic acid (VIA)')
    st.write('- Colposcopy')
    st.write('- Endocervical curettage (ECC)')

    # Food recommendation
    st.header('Food Recommendation')
    st.write('The following foods can help prevent cervical cancer:')
    st.write('- Fruits and vegetables')
    st.write('- Whole grains')
    st.write('- Lean proteins')
    st.write('- Foods rich in folate')
    st.write('- Foods rich in vitamin C')

    # Helplines
    st.header('Helplines')
    st.write('The following helplines provide support for cervical cancer patients:')
    st.write('- National Cancer Society Malaysia (NCSM): 1-800-88-1000')
    st.write('- Pink Ribbon Wellness Foundation: 03-7932 4744')
    st.write('- Malaysian Ministry of Health: 03-8883 4420')
    st.write('- Cancer Research Malaysia: 03-7846 5432')
    st.write('- Hospis Malaysia: 03-9133 3936')

if name == 'main':
  main()
