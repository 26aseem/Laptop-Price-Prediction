import streamlit as st
import pickle
import numpy as np
import pandas as pd

# import the model and the dataframe
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

st.title("Laptop Predictor")

# Brand
company = st.selectbox('Brand', df['Company'].unique())

# Type of Laptop
typename = st.selectbox('Type', df['TypeName'].unique())

# RAM
ram = st.selectbox('RAM(in GB)', [2,4,6,8,12,16,24,32,64])

# Weight
weight = st.number_input('Weight of the Laptop')

# Touchscreen
touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])

# IPS
ips = st.selectbox('IPS', ['No', 'Yes'])

# Screen Size
screen_size = st.number_input('Screen Size')

# Resolution
resolution = st.selectbox('Screen Resolution', ['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', '2880x1800', '2560x1600', '2560x1440', '2304x1440'])

# CPU
cpu = st.selectbox('CPU Brand', df['Cpu brand'].unique())

# HDD
hdd = st.selectbox('HDD(in GB)', [0, 128, 256, 512, 1024, 2048])

# SDD
ssd = st.selectbox('SSD(in GB)', [0, 8, 128, 256, 512, 1024, 2048])

# GPU
gpu = st.selectbox('GPU', df['Gpu brand'].unique())

# OS
os = st.selectbox('OS', df['os'].unique())

if st.button('Predict Price'):
    # query
    # ppi
    ppi = None
    
    # touchscreen
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0
        
    # ips
    if ips == 'Yes':
        ips = 1
    else:
        ips = 0
        
    # resolution
    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5/screen_size
    query = np.array([company, typename, ram, weight, touchscreen, ips,ppi, cpu, hdd, ssd, gpu, os])
    query = query.reshape(1,12)
    
    # Prediction
    st.title("Predicted Price of the Laptp: ₹" + str(int(np.exp(pipe.predict(query)[0]))))
    
    