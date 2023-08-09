import joblib
import numpy as np
import pandas as pd
import time as timer
import seaborn as sns
import streamlit as st

from sklearn import metrics
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.inspection import permutation_importance
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.metrics import classification_report,accuracy_score,confusion_matrix
from sklearn.metrics import auc,roc_auc_score,roc_curve,precision_score,recall_score,f1_score


#model imports
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from xgboost import plot_importance
import xgboost as xgb

# Load the model using the XGBoost native method
loaded_model = xgb.Booster()
loaded_model.load_model('XGBoostTunedModel_v1.6.json')

# Now you can use the loaded_model for prediction


#charts
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots



def main():
    st.title("STROKE PREDICTION AND ANALYSIS USING MACHINE LEARNING")

    if st.button("Prediction"):
        
        st.markdown("Enter the User's Details to predict the occurance of Stroke")
        st.text("Please Enter correct details to get better results")
        
        #Getting User Inputs
        gender = st.radio("What is User's gender",("Male","Female"))
        age = st.number_input("Enter User's age",value=40)
        hypertension = st.radio("Hypertension?",("Yes","No"))
        heart_disease = st.radio("User Ever had a heart disease?",("Yes","No"))
        ever_married = st.radio("User Ever Married?",("Yes","No"))
        work_type = st.radio("What is User's work type?",("Government Job","Private Job","Self Employed","Never Worked","Children"))
        Residence_type = st.radio("What is User's Residence type?",("Urban","Rural"))
        avg_glucose_level = st.number_input("Enter User's Average Glucose Level",value=92.35)
        
        #BMI Calculation with Height and Weight is User doesn't know BMI
        if st.checkbox("Dont Know BMI? Use height and weight"):
            height = st.number_input("Enter User's Height in cm",value=160)
            weight = st.number_input("Enter User's Weight in kgs",value=60)
            bmi = weight / (height/100)**2
            st.write("BMI of user is {:.2f} and will be autoupdated".format(bmi))
        else:
            bmi = st.number_input("Enter User's BMI",value=25.4)

        smoking_status = st.radio("User's Smoking Status?",("Unknown","Formerly Smoked","Never Smoked","Smokes"))
        #Creating nparray of User Inputs
        user_input = np.array([gender,age,hypertension,heart_disease,ever_married,work_type,Residence_type,avg_glucose_level,bmi,smoking_status]).reshape(1,-1)
        # Load the XGBoost model
        trained_model = xgb.Booster()
        trained_model.load_model('XGBoostTunedModel_v1.6.json')

        # Predict using the loaded model
        prediction = trained_model.predict(xgb.DMatrix(user_input))
        if st.button("Submit"):
            #Encoding categorical attributes to values
            gender = 1 if gender == 'Male' else 0
            age = float(age)
            hypertension = 1 if hypertension == 'Yes' else 0
            ever_married = 1 if ever_married == 'Yes' else 0
            heart_disease = 1 if heart_disease == 'Yes' else 0
            if work_type == 'Government Job':
                work_type = 0 
            elif work_type == 'Never Worked':
                work_type = 1 
            elif work_type == 'Private Job':
                work_type = 2 
            elif work_type == 'Self Employed':
                work_type = 3
            elif work_type == 'Children':
                work_type = 4 
            Residence_type = 1 if Residence_type == 'Urban' else 0
            avg_glucose_level = float(avg_glucose_level)
            bmi = float(bmi)
            if smoking_status == 'Unknown':
                smoking_status = 0 
            elif smoking_status == 'Formerly Smoked':
                smoking_status = 1 
            elif smoking_status == 'Never Smoked':
                smoking_status = 2
            elif smoking_status == 'Smokes':
                smoking_status = 3 

            #Creating nparray of User Inputs
            user_input = np.array([gender,age,hypertension,heart_disease,ever_married,work_type,Residence_type,avg_glucose_level,bmi,smoking_status]).reshape(1,-1)
            
            #converting into dataframe to avoid mismatching feature_names error
            user_input = pd.DataFrame(user_input, columns = ['gender', 'age', 'hypertension', 'heart_disease', 'ever_married', 'work_type', 'Residence_type', 'avg_glucose_level', 'bmi', 'smoking_status'])
            
            #prediction using selected model
            prediction = trained_model.predict(user_input)

            #Prediction Probability
            pred_prob = trained_model.predict_proba(user_input)
            stroke_prob = pred_prob[0][1]*100

            #Printing Predicted results
            if prediction == 1:
                st.header("User has Higher Chances of having a Stroke😔")
            else:
                st.header("User has Lower Chances of having a Stroke😊")
            
            #printing prediction probability 
            if stroke_prob < 25:
                st.success("Probability of Occurance of Stroke is {:.2f}%".format(stroke_prob))
            elif stroke_prob < 50:
                st.info("Probability of Occurance of Stroke is {:.2f}%".format(stroke_prob))
            elif stroke_prob < 75:
                st.warning("Probability of Occurance of Stroke is {:.2f}%".format(stroke_prob))
            else:
                st.error("Probability of Occurance of Stroke is {:.2f}%".format(stroke_prob))
            st.text("Predicted with "+prediction_model+" Model with Accuracy of " +model_accuracy)
    
if __name__ == '__main__':
    main()
