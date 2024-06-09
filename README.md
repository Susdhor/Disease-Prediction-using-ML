
# Disease Prediction Using Machine Learning
This repository contains a Streamlit application for predicting diseases such as heart disease, Parkinson's disease, and diabetes using machine learning models. The application allows users to input various health parameters and get predictions based on pre-trained models. This project aims to provide a simple and user-friendly tool for early detection of these diseases, leveraging the power of machine learning

## Overview

In this project, several machine learning models have been developed to predict different diseases based on input features. The goal is to provide an accessible tool for preliminary disease screening, which can be used by healthcare professionals and patients alike.
## Models
# Heart Disease Prediction Model
The heart disease prediction model is trained using a RandomForestClassifier on a dataset containing various health parameters. The dataset includes features such as age, sex, chest pain type, resting blood pressure, cholesterol levels, and more. The model predicts whether an individual has heart disease based on these inputs.

# Parkinson's Disease Prediction Model
The Parkinson's disease prediction model uses a RandomForestClassifier trained on a dataset with features like MDVP (voice measurement parameters), spread1, spread2, D2, PPE, etc. The model predicts whether an individual has Parkinson's disease based on voice measurements and other related parameters.

# Diabetes Prediction Model
The diabetes prediction model is trained using a RandomForestClassifier on a dataset with features like pregnancies, glucose levels, blood pressure, skin thickness, insulin levels, BMI, and more. The model predicts whether an individual has diabetes based on these health parameters.

# Model Training and Saving
The models are trained and saved using the joblib library for later use in the Streamlit application. Below are the sample codes for training and saving the models

## Features

- **Multiple Disease Predictions**: The app can predict multiple diseases based on the input data.
- **User-Friendly Interface**: Built with Streamlit, the web application offers an intuitive and easy-to-use interface.
- **Machine Learning Models**: The project utilizes various machine learning algorithms to ensure accurate predictions.
- **Interactive Input Forms**: Users can input their medical data through interactive forms.

## Getting Started
### Prerequisites

To run this project, you need to have the following installed:

- Python 3.6+
- Streamlit
- scikit-learn
- pandas
- numpy

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/Susdhor/Disease-Prediction-using-ML.git
    cd Disease-Prediction-using-ML
    ```

2. Install the required packages:


### Running the App

To start the web application, use the following command:

```sh
streamlit run app.py
