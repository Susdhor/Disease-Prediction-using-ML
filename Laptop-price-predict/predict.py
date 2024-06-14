
import numpy as np
import streamlit as st
import pickle

# Load the model
with open('C:/Users/susdh/Desktop/Projects ms/Streamlit-App-Diseases-prediction/Laptop-price-predict/pipe.pkl', 'rb') as model_file:
    df_pipe = pickle.load(model_file)

with open('C:/Users/susdh/Desktop/Projects ms/Streamlit-App-Diseases-prediction/Laptop-price-predict/df.pkl', 'rb') as data_file:
    data = pickle.load(data_file)

st.title("Laptop Price Predictor")
# Brand
company = st.selectbox('Brand', data['Company'].unique())

# Type of laptop
type = st.selectbox('Type', data['TypeName'].unique())

# RAM
ram = st.selectbox('RAM (in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])

# Weight
weight = st.number_input('Weight of the Laptop')

# Touchscreen
touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])

# IPS
ips = st.selectbox('IPS', ['No', 'Yes'])

# Screen size
screen_size = st.number_input('Screen Size')

# Resolution
resolution = st.selectbox('Screen Resolution', [
    '1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', '2880x1800', '2560x1600', '2560x1440', '2304x1440'])

# CPU
cpu = st.selectbox('CPU', data['Cpu brand'].unique())

# HDD
hdd = st.selectbox('HDD (in GB)', [0, 128, 256, 512, 1024, 2048])

# SSD
ssd = st.selectbox('SSD (in GB)', [0, 8, 128, 256, 512, 1024])

# GPU
gpu = st.selectbox('GPU', data['Gpu brand'].unique())

# OS
os = st.selectbox('OS', data['os'].unique())

if st.button('Predict Price'):
    # Calculate pixels per inch (PPI)
    ppi = None
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == 'Yes':
        ips = 1
    else:
        ips = 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5 / screen_size

    # Create a query array for the model prediction
    query = np.array([company, type, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os])

    # Reshape the query to fit the model's expected input
    query = query.reshape(1, 12)

    # Predict the price and display it
    predicted_price = np.exp(df_pipe.predict(query)[0])
    st.title(f"The predicted price of this configuration is {int(predicted_price)}")