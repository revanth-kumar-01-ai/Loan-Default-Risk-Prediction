import os  # Importing OS module for system operations
import warnings  # Suppressing warnings
import pandas as pd  # Importing Pandas for data manipulation
import numpy as np  # Importing NumPy for numerical operations

import streamlit as st  # Importing Streamlit for web application
from sklearn.tree import DecisionTreeClassifier as DT  # Importing Decision Tree Classifier

# Streamlit Page Title
st.header("Model Training Page")

code = """
import os  # Importing OS module
import warnings  # Suppressing warnings
import pandas as pd  # Data manipulation
import numpy as np  # Numerical operations

from sklearn.tree import DecisionTreeClassifier as DT  # Decision Tree Classifier

# Load Data
df = pd.read_csv('artifacts/data_transformation/train.csv')  # Reading training data
dfTest = pd.read_csv('artifacts/data_transformation/test.csv')  # Reading test data

# Hide warnings
warnings.filterwarnings('ignore')  # Ignoring warnings

# Split Features and Target Variables
xTrain = df.drop(columns='categorical__default_yes')  # Features for training
yTrain = df['categorical__default_yes']  # Target variable for training

xTest = dfTest.drop(columns='categorical__default_yes')  # Features for testing
yTest = dfTest['categorical__default_yes']  # Target variable for testing

# Train Model
model = DT(criterion='entropy')  # Initializing Decision Tree with entropy criterion
model.fit(xTrain, yTrain)  # Training the model

# Predictions
predictValues = model.predict(xTest)  # Making predictions on test data
"""

st.code(code, language='python')