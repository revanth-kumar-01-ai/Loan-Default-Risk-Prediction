import streamlit as st 


st.header("Loan Default Prediction Dashboard")
st.header("Problem Statement")
st.write(
    "A significant proportion of customers are defaulting on loans, posing financial risks to banks."
)

st.header("Project Overview")
    
st.subheader("1. Business Problem")
st.markdown(
    "- **Business Objectives:** Minimize Loan Defaulters  \n"
    "- **Business Constraints:** Maximize Profits  \n"
    "- **Success Criteria:**  \n"
    "    - **Business success criteria:** Reduce the loan defaulters by 10%  \n"
    "    - **ML success criteria:** Achieve an accuracy of over 92%  \n"
    "    - **Economic success criteria:** Save the bank with > 1.2 MUSD  "
)

st.subheader("2. Data Collection")
st.write("Bank dataset consisting of 1000 customers and 17 variables (16 Inputs and 1 Output)")

st.subheader("3. Data Preprocessing")
st.write("Cleansing & EDA / Descriptive Analytics to ensure data quality.")

st.subheader("4. Model Building")
st.write("Hyperparameter tuning and handling class imbalance.")

st.subheader("5. Evaluation")
st.write("Performance metrics to assess the model’s accuracy and reliability.")

st.subheader("6. Model Deployment")
st.write("Deploying the model using Flask for real-world predictions.")

st.subheader("7. Monitoring & Maintenance")
st.write("Prediction results stored in an MS SQL database for continuous monitoring.")
