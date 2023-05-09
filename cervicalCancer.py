import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
url = 'https://datahub.io/machine-learning/cervical-cancer/r/cervical-cancer.csv'
df = pd.read_csv(url)

# Preprocess the dataset
df = df.drop(['Hinselmann', 'Schiller', 'Citology'], axis=1) # remove unnecessary columns
df = df.replace('?', pd.np.nan).dropna() # handle missing values
df = pd.get_dummies(df, columns=['Age', 'Number of sexual partners', 'First sexual intercourse',
                                 'Num of pregnancies', 'Smokes', 'Smokes (years)', 'Smokes (packs/year)',
                                 'Hormonal Contraceptives', 'Hormonal Contraceptives (years)',
                                 'IUD', 'IUD (years)', 'STDs', 'STDs (number)', 'STDs:condylomatosis',
                                 'STDs:cervical condylomatosis', 'STDs:vaginal condylomatosis', 
                                 'STDs:vulvo-perineal condylomatosis', 'STDs:syphilis', 'STDs:pelvic inflammatory disease',
                                 'STDs:genital herpes', 'STDs:molluscum contagiosum', 'STDs:HIV', 'STDs:Hepatitis B',
                                 'STDs:HPV'], prefix='', prefix_sep='') # encode categorical variables

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df.drop('Biopsy', axis=1), df['Biopsy'], test_size=0.2, random_state=42)

# Train a Random Forest classifier on the training set
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Evaluate the model on the testing set
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
st.write('Accuracy:', accuracy)

# Create a Streamlit web application
st.title('Cervical Cancer Diagnosis')
st.write('Please enter the following information to determine if you have cervical cancer or not:')
age = st.slider('Age', 13, 84, 25)
sexual_partners = st.slider('Number of sexual partners', 0, 28, 5)
first_sexual_intercourse = st.slider('Age at first sexual intercourse', 10, 32, 16)
pregnancies = st.slider('Number of pregnancies', 0, 11, 2)
smokes = st.radio('Do you smoke?', ['Yes', 'No'])
smokes_years = st.slider('How many years have you smoked?', 0, 37, 5)
smokes_packs_per_year = st.slider('How many packs of cigarettes do you smoke per year?', 0, 150, 10)
hormonal_contraceptives = st.radio('Do you use hormonal contraceptives?', ['Yes', 'No'])
hormonal_contraceptives_years = st.slider('How many years have you used hormonal contraceptives?', 0, 35, 5)
iud = st.radio('Do you use intrauterine device (IUD)?', ['Yes', 'No'])
iud_years = st.slider('How many years have you used intrauterine device (IUD)?', 0, 20, 5)
