import streamlit as st
import pandas as pd
import requests
from io import StringIO

st.title("Loan Prediction Application")
st.write("Upload a CSV file to get loan predictions.")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read CSV file
    file_content = uploaded_file.getvalue().decode("utf-8")
    df = pd.read_csv(StringIO(file_content))
    
    st.subheader("Uploaded Data")
    st.dataframe(df)  # Display uploaded data
    
    # API URL
    api_url = "https://ml-models-app.onrender.com/loan_prediction"
    

    with st.spinner("Fetching prediction... Please wait."):
        try:
            response = requests.post(api_url, files={"file": uploaded_file})
            response.raise_for_status()  # Raise error for bad responses (4xx, 5xx)
            loan_result = response.json()
            
            st.subheader("Loan Prediction Result")
            st.json(loan_result)
        except requests.exceptions.RequestException as e:
            st.error(f"Error fetching prediction: {e}")
