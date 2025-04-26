#!/usr/bin/env python
# coding: utf-8

# In[17]:

import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

st.set_page_config(layout="wide")
st.image('dark_horse.png', use_column_width=True)
st.title("Calorie Burn Predictor")

#Layout: form on the left, prediction on the right
col1, col2 = st.columns([2, 1])  # Adjust width ratio if needed

with col1:
    st.header("Enter Your Details")
    with st.form("my_form"):
        Gender = st.selectbox('Select your Gender', ['Male', 'Female'])
        Session_Duration = st.number_input('Session Duration (hours)', value=0.0, format="%.2f")
        Fat_Percentage = st.number_input('Fat Percentage (%)', value=0.0, format="%.2f")
        Workout_Frequency = st.number_input('Workout Frequency (days/week)', value=0.0, format="%.2f")
        Experience_Level = st.number_input('Experience Level (e.g., 1–5)', value=0.0, format="%.2f")
        
        submit = st.form_submit_button('Predict Calories Burned')

with col2:
    st.header("Prediction")
    if submit:
        gender_map = {'Male': 0, 'Female': 1}
        gender_val = gender_map[Gender]

        input_df = pd.DataFrame([[Session_Duration, Fat_Percentage, Workout_Frequency, Experience_Level, gender_val]],
                                columns=['Session_Duration (hours)', 'Fat_Percentage', 'Workout_Frequency (days/week)', 'Experience_Level', 'Gender'])

        # Scale the numeric features
        scaled_values = scaler.transform(input_df.drop('Gender', axis=1))

        # Combine with Gender
        input_array = np.column_stack((scaled_values, input_df['Gender'].values))
        
        if Workout_Frequency < 1:
            st.write("Workout Frequency must be at least 1 day/week.")
        elif Session_Duration <= 0 or Fat_Percentage <= 0:
            st.write("please enter a value greater than 0 in the Session Duration and Fat Percentage fields")
        else:
            prediction = model.predict(input_array)
            predicted_value = max(prediction[0], 0)
            if predicted_value < 500:
                st.info(f"Calories Burned: {predicted_value:,.2f} \n\nit looks like you need to put in a bit more effort to see results 😅. Try increasing your session duration")
            elif 500 <= predicted_value < 1000:
                st.info(f"Calories Burned: {predicted_value:,.2f} \n\nNice work! You're making progress. Keep it up and push a little more to hit that next milestone!")
            else:
                st.success(f"Calories Burned: {predicted_value:,.2f} \n\nAmazing! You're smashing your workouts. Keep that energy high and stay consistent!")
    else:
        st.info("Fill the form and click submit to see prediction.")

# In[ ]:




