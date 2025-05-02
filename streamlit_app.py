#!/usr/bin/env python
# coding: utf-8

# In[44]:


import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

model = pickle.load(open('best_rf_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))
wf_label_encoder = pickle.load(open('wf_label_encoder.pkl', 'rb'))
el_label_encoder = pickle.load(open('el_label_encoder.pkl', 'rb'))

st.set_page_config(layout="wide")
st.image('darkhorse.png', use_column_width=True)
st.title("Calorie Burn Predictor")

#Layout: form on the left, prediction on the right
col1, col2 = st.columns([1.5, 1.5])  # Adjust width ratio if needed

with col1:
    st.header("Enter Your Details")
    with st.form("my_form"):
        #Gender = st.selectbox('Gender', ['Male', 'Female'])
        Avg_BPM = st.number_input('Avg_BPM', value=0.0, format="%.2f")
        Session_Duration = st.number_input('Session Duration (hours)', value=0.0, format="%.2f")
        Fat_Percentage = st.number_input('Fat Percentage (%)', value=0.0, format="%.2f")
        Workout_Frequency = st.selectbox('Workout Frequency (days/week)', [2, 3, 4, 5])
        Experience_Level = st.selectbox('Experience Level', [1, 2, 3,])
        
        submit = st.form_submit_button('Predict Calories Burned')

with col2:
    st.header("Prediction")
    if submit:
        input_df = pd.DataFrame([[Avg_BPM, Session_Duration, Fat_Percentage, Workout_Frequency, Experience_Level]],
                                columns=['Avg_BPM', 'Session_Duration (hours)', 'Fat_Percentage', 'Workout_Frequency (days/week)', 'Experience_Level'])

        #input_encoded = pd.get_dummies(input_df, columns=['Gender'], drop_first=True).astype('int')
        input_encoded = input_df.copy()
        input_encoded['Workout_Frequency (days/week)'] = wf_label_encoder.transform(input_encoded['Workout_Frequency (days/week)'])
        input_encoded['Experience_Level'] = el_label_encoder.transform(input_encoded['Experience_Level'])
        
        expected_cols = ['Avg_BPM', 'Session_Duration (hours)', 'Fat_Percentage',
                         'Workout_Frequency (days/week)','Experience_Level']

        for col in expected_cols:
            if col not in input_encoded.columns:
                input_encoded[col] = 0
        input_encoded = input_encoded[expected_cols]

        #continuous_cols = ['Avg_BPM', 'Session_Duration (hours)', 'Fat_Percentage']
        #dummy_cols = [col for col in input_encoded.columns if col not in continuous_cols]
        
        #input_cont_scaled = scaler.transform(input_encoded[continuous_cols])
        #input_scaled = np.hstack([input_cont_scaled, input_encoded[dummy_cols].values])
        #input_scaled = scaler.transform(input_encoded)
        

        if Session_Duration <= 0 or Fat_Percentage <= 0:
            st.write("Please enter a value greater than 0 in the Session Duration and Fat Percentage fields.")
        else:
            prediction = model.predict(input_encoded)
            predicted_value = max(prediction[0], 0)
            if predicted_value < 500:
                st.info(f"Calories Burned: {predicted_value:,.2f} \n\nIt looks like you need to put in a bit more effort to see results 😅. Try increasing your session duration!")
            elif 500 <= predicted_value < 1000:
                st.info(f"Calories Burned: {predicted_value:,.2f} \n\nNice work! You're making progress. Keep it up and push a little more to hit that next milestone!")
            else:
                st.success(f"Calories Burned: {predicted_value:,.2f} \n\nAmazing! You're smashing your workouts. Keep that energy high and stay consistent!")
    else:
        st.info("Fill the form and click submit to see prediction.")


# In[ ]:




