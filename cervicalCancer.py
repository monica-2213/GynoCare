import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# Load the dataset
url = "https://datahub.io/machine-learning/cervical-cancer/r/cervical-cancer.csv"
df = pd.read_csv(url)

# Preprocess the data
df = df.replace("?", np.nan)
df = df.dropna()
le = LabelEncoder()
df['Dx:Cancer'] = le.fit_transform(df['Dx:Cancer'])

# Train the model
features = ['Age', 'Number of sexual partners', 'First sexual intercourse', 'Num of pregnancies', 'Smokes', 'Smokes (years)', 'Smokes (packs/year)', 'Hormonal Contraceptives', 'Hormonal Contraceptives (years)', 'IUD', 'IUD (years)', 'STDs', 'STDs (number)', 'STDs:condylomatosis', 'STDs:cervical condylomatosis', 'STDs:vaginal condylomatosis', 'STDs:vulvo-perineal condylomatosis', 'STDs:syphilis', 'STDs:pelvic inflammatory disease', 'STDs:genital herpes', 'STDs:molluscum contagiosum', 'STDs:AIDS', 'STDs:HIV', 'STDs:Hepatitis B', 'STDs:HPV', 'STDs: Number of diagnosis', 'Dx:Cancer', 'Dx:CIN', 'Dx:HPV', 'Dx']

X = df[features]
y = df['Dx:Cancer']

model = RandomForestClassifier()
model.fit(X, y)

# Create the Streamlit app
st.title('Cervical Cancer Expert System')

# Collect input from the user
age = st.slider('What is your age?', 15, 84)
sexual_partners = st.slider('How many sexual partners have you had?', 0, 30)
first_sexual_intercourse = st.slider('At what age did you have your first sexual intercourse?', 10, 40)
pregnancies = st.slider('How many times have you been pregnant?', 0, 10)
smoking = st.radio('Do you smoke?', ('Yes', 'No'))
if smoking == 'Yes':
    smoking_years = st.slider('For how many years have you smoked?', 0, 50)
    smoking_packs = st.slider('How many packs of cigarettes per year do you smoke?', 0, 5)
else:
    smoking_years = 0
    smoking_packs = 0
contraceptives = st.radio('Have you used hormonal contraceptives?', ('Yes', 'No'))
if contraceptives == 'Yes':
    contraceptive_years = st.slider('For how many years have you used hormonal contraceptives?', 0, 50)
else:
    contraceptive_years = 0
iud = st.radio('Have you used an IUD?', ('Yes', 'No'))
if iud == 'Yes':
    iud_years = st.slider('For how many years have you used an IUD?', 0, 50)
else:
    iud_years = 0
stds = st.radio('Have you ever had a sexually transmitted disease?', ('Yes', 'No'))
if stds == 'Yes':
    stds_num = st.slider('How many sexually transmitted diseases have you had?', 0, 5)
    stds_cond = st.checkbox('Condylomatosis')
    stds_cervical_cond = st.checkbox('Cervical Condylomatosis')
    stds_vaginal_cond = st.checkbox('Vaginal Condylomatosis')
    stds_vulvo_cond = st.checkbox('Vulvo-perineal Condylomatosis')
    stds_syphilis = st.checkbox('Syphilis')
    stds_pid = st.checkbox('Pelvic Inflammatory Disease')
    stds_herpes = st.checkbox('Genital Herpes')
    stds_molluscum = st.checkbox('Molluscum Contagiosum')
    stds_aids = st.checkbox('AIDS')
    stds_hiv = st.checkbox('HIV')
    stds_hepatitis = st.checkbox('Hepatitis B')
    stds_hpv = st.checkbox('HPV')
    stds_diagnosis = st.slider('How many diagnoses of sexually transmitted diseases have you had?', 0, 5)
else:
    stds_num = 0
    stds_cond = False
    stds_cervical_cond = False
    stds_vaginal_cond = False
    stds_vulvo_cond = False
    stds_syphilis = False
    stds_pid = False
    stds_herpes = False
    stds_molluscum = False
    stds_aids = False
    stds_hiv = False
    stds_hepatitis = False
    stds_hpv = False
    stds_diagnosis = 0

# Make predictions with the model
data = {
    'Age': age,
    'Number of sexual partners': sexual_partners,
    'First sexual intercourse': first_sexual_intercourse,
    'Num of pregnancies': pregnancies,
    'Smokes': smoking == 'Yes',
    'Smokes (years)': smoking_years,
    'Smokes (packs/year)': smoking_packs,
    'Hormonal Contraceptives': contraceptives == 'Yes',
    'Hormonal Contraceptives (years)': contraceptive_years,
    'IUD': iud == 'Yes',
    'IUD (years)': iud_years,
    'STDs': stds == 'Yes',
    'STDs (number)': stds_num,
    'STDs:condylomatosis': stds_cond,
    'STDs:cervical condylomatosis': stds_cervical_cond,
    'STDs:vaginal condylomatosis': stds_vaginal_cond,
    'STDs:vulvo-perineal condylomatosis': stds_vulvo_cond,
    'STDs:syphilis': stds_syphilis,
    'STDs:pelvic inflammatory disease': stds_pid,
    'STDs:genital herpes': stds_herpes,
    'STDs:molluscum contagiosum': stds_molluscum,
    'STDs:AIDS': stds_aids,
    'STDs:HIV': stds_hiv,
    'STDs:Hepatitis B': stds_hepatitis,
    'STDs:HPV': stds_hpv,
    'STDs: Number of diagnosis': stds_diagnosis
}
X_new = pd.DataFrame(data, index=[0])
y_pred = model.predict(X_new)

# Display the prediction to the user
if y_pred[0] == 0:
  st.write('Based on the information you provided, it is unlikely that you have cervical cancer.')
else:
  st.write('You are fine')
