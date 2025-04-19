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

st.set_page_config(layout='wide')
st.image('dark_horse.png', use_column_width=True)
st.sidebar.write('**Input Parameters**')

with st.sidebar.form("my_form"):
    Gender = st.selectbox('Select your Gender', ['Male', 'Female'])
    Session_Duration = st.number_input('Enter your Session Duration (hours)', value=0.0, format="%.2f")
    Fat_Percentage = st.number_input('Enter your Fat Percentage (%)', value=0.0, format="%.2f")
    Workout_Frequency = st.number_input('Enter your Workout Frequency (days/week)', value=0.0, format="%.2f")
    Experience_Level = st.number_input('Enter your Experience Level (e.g., 1–5)', value=0.0, format="%.2f")

    submit = st.form_submit_button('Submit')

gender_map = {'Male': 0, 'Female': 1}
gender_val = gender_map[Gender]

if submit:
    input_df = pd.DataFrame([[Session_Duration, Fat_Percentage, Workout_Frequency, Experience_Level, gender_val]],
                            columns=['Session_Duration (hours)', 'Fat_Percentage', 'Workout_Frequency (days/week)', 'Experience_Level', 'Gender'])

    scaled_values = scaler.transform(input_df.drop('Gender', axis=1))
    input_array = np.column_stack((input_df['Gender'].values, scaled_values))
    prediction = model.predict(input_array)

    st.subheader("Predicted Calories Burned:")
    st.success(f"{prediction[0]:,.2f} calories")


# In[ ]:




