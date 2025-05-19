# Calories Burn Predictor

## project demo link - https://calorypredictor.streamlit.app/
![Alt text](images/darkhorse.png)

calories burn prediction involves estimating the number of calories likely to be burned during a gym session based on user input such as Average BPM, session duration, workout frequency and Fat percentage. This is a critical tool for gyms aiming to motivate new clients and retain existing ones by giving personalized insights into their fitness journey.

**Why Is It Important?**

For most individuals joining a gym, calorie burn is a primary goal. From a business perspective, providing potential and current clients with realistic and personalized projections can serve as a powerful motivator. It can also enhance client acquisition by setting clear, data-backed expectations.

**About the Dataset**  
The dataset contains 963 records and 15 features, representing both past and current gym clients. The goal is to predict the number of calories burned in a single session, which helps the business in:  
Personalizing client experiences  
Boosting client motivation  
Enhancing client retention and onboarding strategies  

**Steps Involved in Model development & Deployment**  
descriptive analysis to extract key insights from the data using power BI  
the link to the dashboard - [Power BI Dashboard](https://app.powerbi.com/links/jiRad3E2nE?ctid=06815d30-c3a7-41f1-ae74-0fda03852c96&pbi_source=linkShare)  
Data Preprocessing  
Feature Engineering  
Feature Selection using statistical tests and feature importance
Model Training with Random Forest Regressor 
Hyperparameter Tuning using GridSearchCV  
Model Serialization with Pickle  
Web Application Development using Streamlit  
Deployment on Streamlit Community Cloud  

**Packages Used**  
This project uses Python and the following libraries:  
numpy  
pandas  
matplotlib  
seaborn  
scikit-learn  
scipy  
streamlit  
pickle  

**Project Objective**  
To build a Random Forest Regressor model that accurately predicts the calories burned during a gym session based on client input. 

**Evaluation Metric**

The model's performance was evaluated using Root Mean Squared Error (RMSE), resulting in a value of 65.32 calories. This indicates that, on average, the model's predictions deviate from the actual calorie burn by approximately 65.32 calories, which represents a relative error of 7.23% compared to the mean actual calorie burn.

Project Demo Link - [Click Here](https://calorypredictor.streamlit.app/)


