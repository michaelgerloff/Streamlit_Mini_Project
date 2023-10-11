import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Prediction of maliciousness of websites')    
st.write("upload your website metadata to get a prediction of it's maliciousness")
url = st.text_input('Enter the URL of the website you want to check', "URL")
st.write('The URL you entered is: ', url)

st.selectbox("Please select the Charset:",("Utf-8", "Iso-8859-1", "Windows-1252"))
st.selectbox("Please select the country:",("US", "CA", "GB", "None"))

for i in dict:
    st.slider(i, min_value=None, max_value=None)
    
st.button('Predict')