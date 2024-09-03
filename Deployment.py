# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 13:01:17 2020

"""

import pandas as pd
import streamlit as st 
from sklearn.linear_model import LogisticRegression
import pickle as pickle

st.title('Deployment')

st.sidebar.header('Input Parameters')

def user_input_features():
    Pclass= st.sidebar.selectbox('Class',('1','2','3'))
    Sex_male= st.sidebar.selectbox('Sex',('0','1'))
    Age= st.sidebar.number_input('Insert Age')
    SibSp = st.sidebar.selectbox('SibSp',('0','1','2','3'))
    Parch= st.sidebar.selectbox('Parch',('0','1','2','3','4','5','6'))
    Fare= st.sidebar.number_input('Insert Fare')
    Embarked_Q= st.sidebar.selectbox('Embarked_Q',('0','1'))
    Embarked_S= st.sidebar.selectbox('Embarked_S',('0','1'))
    
   
    
    data= {'Pclass':Pclass,
            'Age':Age,
            'SibSp':SibSp,
            'Parch':Parch,
            'Fare':Fare,
            'Sex_male':Sex_male,
            'Embarked_Q':Embarked_Q,
            'Embarked_S':Embarked_S}

    features = pd.DataFrame(data,index = [0])
    return features 
    
User_input= user_input_features()
st.subheader('Input parameters')
st.write(User_input)

loaded_model=pickle.load(open("C:\\Users\\abhil\\Downloads\\Assignments\\logistic.pkl",'rb'))


prediction = loaded_model.predict(User_input)
prediction_proba = loaded_model.predict_proba(User_input)

   

st.subheader('Result')
if prediction==0:
    st.write("Not survive")
else:
    st.write("Survive")
             

st.subheader('Probability')
st.write(prediction_proba)
