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

st.write(col_order)
output= {}

for key, value in category.items():
    output[key] = st.selectbox("Please select the " + key + ":", value)
    




for key, value in numerical.items():
    if key != 'DNS_QUERY_TIMES':
        output[key]= int(st.slider(key, min_value=0, max_value=int(value[1]*2)))
    else:
        output[key]= float(st.slider(key, min_value=0.0, max_value=(value[1]*2)))
    
if st.button('Predict'):
    sorted_dict = {key: output[key] for key in col_order.values()}
    df_output = pd.DataFrame(sorted_dict, index=[0])
    st.write(df_output.dtypes)
    st.write(df_output)
    xgboost_pipeline.predict(df_output)
    st.write('The website with the URL ', url, 'is malicious with a probability of ', 0.5)