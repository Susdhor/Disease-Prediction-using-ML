
# Laptop Price Prediction

This project aims to predict the prices of laptops based on their specifications. It includes data preparation, model creation, and a Streamlit application for easy user interaction. The project is divided into several key components:

1. **Data Preparation**: The dataset is cleaned and preprocessed to ensure it is suitable for model training.
2. **Model Creation**: A machine learning model is trained to predict laptop prices.
3. **Model Saving**: The trained model and the prepared data are saved for future use.
4. **Streamlit Application**: A user-friendly web application is built using Streamlit to allow users to predict laptop prices based on input specifications.

## Project Structure

- `df/`: Contains the dataset used for training the model.
- `price_predict (notebooks)/`: Jupyter notebooks for data preparation and model training.
- `pipe/`: Saved model files and preprocessed data.
- `predict.py/`: Streamlit application files for price prediction.
- `README.md`: Project documentation.

## Notebooks

### Data Preparation and Model Training (`notebooks/price_predict.ipynb`)

This notebook covers:
- Data loading and initial exploration.
- Data cleaning and preprocessing.
- Feature engineering.
- Model training and evaluation.
- Saving the trained model and preprocessed data.

### Streamlit Application (`app/predict.py`)

This script:
- Loads the saved model and data.
- Creates a web application using Streamlit.
- Allows users to input laptop specifications.
- Predicts the laptop price based on the input specifications.

## How to Run the Project

### Prerequisites

- Python 3.7 or higher
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- ML algorithms

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/laptop-price-prediction.git
   cd laptop-price-prediction
### Usage
- Open the Streamlit application.
- Enter the specifications of the laptop you want to price (e.g., brand, processor, RAM, storage, etc.).
- Click the "Predict" button to get the estimated price of the laptop.


### License
- This project is licensed under the MIT License. See the ´LICENSE´ file for details.