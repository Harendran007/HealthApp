import streamlit as st
import pandas as pd
import joblib

model = joblib.load('random_forest_model.pkl')

def predict_heart_disease(data):
    prediction = model.predict(data)
    return prediction

def main():
    st.title('Heart Disease Prediction')
    age = st.slider('Age', min_value=0, max_value=100, value=50)
    sex = st.radio('Sex', ['Male', 'Female'])
    cp = st.selectbox('Chest Pain Type', [0, 1, 2, 3])
    trestbps = st.slider('Resting Blood Pressure', min_value=0, max_value=200, value=120)
    chol = st.slider('Cholesterol (mg/dl)', min_value=0, max_value=600, value=200)
    fbs = st.radio('Fasting Blood Sugar > 120 mg/dl', ['No', 'Yes'])
    restecg = st.selectbox('Resting Electrocardiographic Results', [0, 1, 2])
    thalach = st.slider('Maximum Heart Rate Achieved', min_value=0, max_value=300, value=150)
    exang = st.radio('Exercise Induced Angina', ['No', 'Yes'])
    oldpeak = st.slider('ST Depression Induced by Exercise Relative to Rest', min_value=0.0, max_value=10.0, value=0.0)
    slope = st.selectbox('Slope of the Peak Exercise ST Segment', [0, 1, 2])
    ca = st.selectbox('Number of Major Vessels Colored by Flourosopy', [0, 1, 2, 3])
    thal = st.selectbox('Thalassemia', [0, 1, 2, 3])

    if st.button('Predict'):
        sex_encoded = 1 if sex == 'Male' else 0
        fbs_encoded = 1 if fbs == 'Yes' else 0
        exang_encoded = 1 if exang == 'Yes' else 0

        input_data = pd.DataFrame({'age': [age], 'sex': [sex_encoded], 'cp': [cp], 'trestbps': [trestbps],
                                   'chol': [chol], 'fbs': [fbs_encoded], 'restecg': [restecg],
                                   'thalach': [thalach], 'exang': [exang_encoded], 'oldpeak': [oldpeak],
                                   'slope': [slope], 'ca': [ca], 'thal': [thal]})

        prediction = predict_heart_disease(input_data)
        if prediction[0] == 1:
            st.write("The patient is likely to have heart disease.")
        else:
            st.write("The patient is unlikely to have heart disease.")

if __name__ == '__main__':
    main()
