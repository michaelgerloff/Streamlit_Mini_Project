import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
import joblib

xgboost_pipeline = joblib.load("./models/encoding_xgboost.pkl")
    
with open("./data/interim/feature_values.pkl", "rb") as f:
    loaded_list = pickle.load(f)
    
st.title('Prediction of maliciousness of websites')    
st.write("upload your website metadata to get a prediction of it's maliciousness")
url = st.text_input('Enter the URL of the website you want to check', "URL")
st.write('The URL you entered is: ', url)

category = loaded_list[1]
numerical = loaded_list[0]
col_order = loaded_list[2]

output= {}

for key, value in category.items():
    output[key] = st.selectbox("Please select the " + key + ":", value)
    




for key, value in numerical.items():
    if key != 'DNS_QUERY_TIMES':
        output[key]= int(st.slider(key, min_value=0, max_value=int(value[1]*2)))
    else:
        output[key]= float(st.slider(key, min_value=0.0, max_value=(value[1]*2)))
    
if st.button('Predict'):
    df_output = pd.DataFrame(output, index=[0])
    df_output = df_output[list(col_order.values())[0]]
    malicious = xgboost_pipeline.predict(df_output)
    if malicious:
        prob = xgboost_pipeline.predict_proba(df_output)[0,1]
        st.write('The website with the URL ', url, 'is malicious with a probability of ', prob, ".")
    else:
        prob = xgboost_pipeline.predict_proba(df_output)[0,0]
        st.write('The website with the URL ', url, 'is not malicious with a probability of ', prob, ".")