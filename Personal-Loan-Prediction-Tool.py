# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle
import streamlit as st

# Loading the Model
loaded_model = pickle.load(open('C:/Users/Ilone/02. DATA MODELLING/model.sav', 'rb'))

# Making the Predictive Function
def loan_pred(input_data):
    input_data_arr = np.asarray(input_data)
    input_data_reshaped = input_data_arr.reshape(1,-1)
    pred = loaded_model.predict(input_data_reshaped)
    print(pred)
    
    if(pred[0]==0):
        return 'Personal loan DITOLAK'
    else:
        return 'Personal loan DITERIMA'

def main():
    # Generating the Title
    st.title('Personal Loan Acceptance Prediction Tool')
    
    # Obtaining the Input Data
    Education = st.text_input('Education Level (1: Undergrad; 2: Graduate; 3: Advanced/Professional)')
    Income = st.text_input('Annual Income ($000)')
    Family= st.text_input('Family Size')
    CCAvg = st.text_input('Average Spending on Credit Cards per Month ($000)')
    Age = st.text_input('Age of the Customer')
    
    # Button for Prediction
    loan = ''
    if st.button('Personal Loan Prediction Result'):
        loan = loan_pred([Education, Income, Family, CCAvg, Age])
    st.success(loan)
    
if __name__ == '__main__':
    main()