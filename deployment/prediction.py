import streamlit as st
import pandas as pd
import numpy as np
import joblib

def app():
    # Text title
    st.write(' # Model Inference of Student Depression')

    # Load the Model
    best_model = joblib.load('best_model.pkl')

    # Create a new dataframe
    df_new = {
        'Age': st.text_input(key = 1, label = 'Age'),
        'Academic Pressure': st.number_input(key = 2, label = 'Academic Pressure', min_value = 0, max_value = 5, step = 1),
        'CGPA': st.number_input(key = 3, label = 'CPGA', step = 1),
        'Study Satisfaction': st.number_input(key = 4, label = 'Study Satisfaction', min_value = 0, max_value = 5, step = 1),
        'Job Satisfaction': st.number_input(key = 5, label = 'Job Satisfaction', min_value = 0, max_value = 4, step = 1),
        'Work/Study Hours': st.number_input(key = 6, label = 'Work/Study Hours', min_value = 0, max_value = 12, step = 1),
        'Gender': st.selectbox(key = 7,
            label = 'Gender',
            options = ['Male', 'Female']
        ),
        'City': st.text_input(key = 8, label = 'City'),
        'Profession': st.text_input(key = 9, label = 'Profession'),
        'Work Pressure': st.selectbox(key = 10,
            label = 'Work Pressure',
            options = ['0.0', '2.0', '5.0']
        ),
        'Sleep Duration': st.selectbox(key = 11,
            label = 'Sleep Duration',
            options = ['Less than 5 hours', '5-6 hours', '7-8 hours', 'More than 8 hours', 'Others']
        ),
        'Dietary Habits': st.selectbox(key = 12,
            label = 'Dietary Habits',
            options = ['Healthy', 'Moderate', 'Unhealthy', 'Others']
        ),
        'Degree': st.text_input(key = 13, label = 'Degree'),
        'Have you ever had suicidal thoughts ?': st.selectbox(key = 14,
            label = 'Had suicidal thoughts?',
            options = ['Yes', 'No']
        ),
        'Financial Stress': st.text_input(key = 15, label = 'Financial Stress'),
        'Family History of Mental Illness': st.selectbox(key = 16,
            label = 'Family History of Mental Illness',
            options = ['Yes', 'No']
        )
    }

    # Convert to Dataframe pandas
    df_new = pd.DataFrame([df_new])

    # Show the output
    st.write(df_new)

    # Prediction button
    if st.button('Predict'):
        prediction = best_model.predict(df_new)

        # Output the prediction
        st.subheader('Prediction Result')
        st.write(f"Prediction: **{'Depressed' if prediction[0] == 1 else 'Not Depressed'}**")

if __name__ == '__main__':
    app()