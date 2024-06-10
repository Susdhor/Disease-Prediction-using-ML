
# load the important dependensis
import streamlit as st
import pickle
import os
from streamlit_option_menu import option_menu


# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")


# loading the saved models

Diabetes_model = pickle.load(open(
    'C:/Users/susdh/Desktop/Projects ms/Streamlit-App-Diseases-prediction/saved-models/diabetic_model.sav', 'rb'))
Hearts_model = pickle.load(open(
    'C:/Users/susdh/Desktop/Projects ms/Streamlit-App-Diseases-prediction/saved-models/heart_model.sav', 'rb'))
Parkinsons_model = pickle.load(open(
    'C:/Users/susdh/Desktop/Projects ms/Streamlit-App-Diseases-prediction/saved-models/parkinson_model.sav', 'rb'))


# Define the options for the dropdown menu
options = ['Diabetes Prediction',
           'Heart Health Check',
           'Parkinsons Risk Test']

# Display the options in the sidebar with a unique subheader
with st.sidebar:
    st.subheader("Prediction for Various Diseases")
    selected_option = option_menu("Select a Disease", options, menu_icon='hospital-fill',
                                  icons=['activity', 'heart-pulse-fill', 'person-check'], default_index=0)


# Function to perform diabetes prediction

def predict_diabetes(Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age):
    user_input = [Pregnancies, Glucose, BloodPressure,
                  SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
    user_input = [float(x) for x in user_input]
    diab_prediction = Diabetes_model.predict([user_input])
    if diab_prediction[0] == 1:
        diab_diagnosis = 'The person is diabetic'
    else:
        diab_diagnosis = 'The person is not diabetic'
    return diab_diagnosis


# Diabetes Prediction Page
if selected_option == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Test Prediction')

    # Image
    st.image('diabetics-test-image.jpg', use_column_width=True)

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input('Number of Pregnancies', value=0)

    with col2:
        Glucose = st.number_input('Glucose Level', value=0)

    with col3:
        BloodPressure = st.number_input('Blood Pressure value', value=0)

    with col1:
        SkinThickness = st.number_input('Skin Thickness value', value=0)

    with col2:
        Insulin = st.number_input('Insulin Level', value=0)

    with col3:
        BMI = st.number_input('BMI value', value=0.0)

    with col1:
        DiabetesPedigreeFunction = st.number_input(
            'Diabetes Pedigree Function value', value=0.0)

    with col2:
        Age = st.number_input('Person Age', value=0)

    # code for Prediction
    diab_diagnosis = ''

    # Button to trigger diabetes test prediction
    if st.button('Diabetes Test Result'):
        # Perform diabetes prediction
        diab_diagnosis = predict_diabetes(
            Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age)
        # Display the result
        st.success(diab_diagnosis)


# 2. Heart Disease Prediction Page
if selected_option == 'Heart Health Check':

    # page title
    st.title('Heart Disease Analysis')

    # add heart image
    st.image('Heart-disease.jpg', use_column_width=True)

    # getting input data from user
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input('Age', value=0)

    with col2:
        sex = st.number_input('Sex', value=0)

    with col3:
        cp = st.number_input('Chest Pain types', value=0)

    with col1:
        trestbps = st.number_input('Resting Blood Pressure', value=0)

    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl', value=0)

    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl', value=0)

    with col1:
        restecg = st.number_input(
            'Resting Electrocardiographic results', value=0)

    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved', value=0)

    with col3:
        exang = st.number_input('Exercise Induced Angina', value=0)

    with col1:
        oldpeak = st.number_input(
            'ST depression induced by exercise', value=0.0)

    with col2:
        slope = st.number_input(
            'Slope of the peak exercise ST segment', value=0)

    with col3:
        ca = st.number_input('Major vessels colored by flourosopy', value=0)

    with col1:
        thal = st.number_input(
            'thal: 0 = normal; 1 = fixed defect; 2 = reversable defect', value=0)

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs,
                      restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = Hearts_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)


# Parkinson's Prediction Page
if selected_option == "Parkinsons Risk Test":

    # page title
    st.title("Parkinson's Awareness: Get Tested Today")

    # add a image on web page
    st.image('Parkinsons-image.jpg', use_column_width=True)

    # get input from user
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.number_input(
            'MDVP Fo(Hz): Median frequency (in Hz)', value=0.0)

    with col2:
        fhi = st.number_input(
            'MDVP Fhi(Hz) : Highest frequency (in Hz)', value=0.0)

    with col3:
        flo = st.number_input(
            'MDVP Flo(Hz): Lowest frequency (in Hz)', value=0.0)

    with col4:
        Jitter_percent = st.number_input(
            'MDVP Jitter(%): Jitter percentage', value=0.0)

    with col5:
        Jitter_Abs = st.number_input(
            'MDVP Jitter(Abs): Absolute Jitter', value=0.0)

    with col1:
        RAP = st.number_input(
            'MDVP RAP : Relative amplitude perturbation', value=0.0)

    with col2:
        PPQ = st.number_input(
            'MDVP PPQ: Pitch period perturbation quotient', value=0.0)

    with col3:
        DDP = st.number_input('Jitter DDP', value=0.0)

    with col4:
        Shimmer = st.number_input('MDVP Shimmer', value=0.0)

    with col5:
        Shimmer_dB = st.number_input('MDVP Shimmer(dB)', value=0.0)

    with col1:
        APQ3 = st.number_input('Shimmer APQ3', value=0.0)

    with col2:
        APQ5 = st.number_input('Shimmer APQ5', value=0.0)

    with col3:
        APQ = st.number_input('MDVP APQ', value=0.0)

    with col4:
        DDA = st.number_input('Shimmer DDA', value=0.0)

    with col5:
        NHR = st.number_input('NHR : Noise-to-harmonics ratio', value=0.0)

    with col1:
        HNR = st.number_input('HNR: Harmonics-to-noise ratio', value=0.0)

    with col2:
        RPDE = st.number_input(
            'RPDE: Recurrence period density entropy', value=0.0)

    with col3:
        DFA = st.number_input('DFA: Detrended fluctuation analysis', value=0.0)

    with col4:
        spread1 = st.number_input('spread1', value=0.0)

    with col5:
        spread2 = st.number_input('spread2', value=0.0)

    with col1:
        D2 = st.number_input('D2', value=0.0)

    with col2:
        PPE = st.number_input('PPE', value=0.0)

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = Parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
