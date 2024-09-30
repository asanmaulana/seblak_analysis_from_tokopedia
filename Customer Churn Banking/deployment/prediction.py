import streamlit as st
import pandas as pd
import numpy as np
import pickle


#Load All files

with open ('best_model.pkl','rb') as file:
    model = pickle.load(file)



def run():
    # Menambahkan judul
    st.title('Customer Churn Prediction')

    st.write("Welcome to the Customer Churn Prediction tool of Bank BNP Paribas. Please fill in the details in the form below to predict the likelihood of a customer churning.")
  #kita buat form untuk isi data
    with st.form('form_customer_example'):
        #gunakan text_input
        name = st.text_input('Surname: ', value = 'Name')
        #pake number_input
        CreditScore = st.number_input('CreditScore: ', value = 0, help = 'Fill with the credit score')
        geography = st.selectbox('Geography: ', ('France', 'Germany','Spain'), index=1)

        gender = st.selectbox('Gender: ', ('Female', 'Male'), index=1)
        #price
        age = st.number_input('Age: ', value = 30, min_value = 0,max_value=100)
        st.markdown('---')

        tenure = st.number_input('Tenure: ', min_value = 0, value = 3, help= 'How long the customer did use our product?')
        balance = st.number_input('Balance: ', min_value = 0, value = 100000)
        numofproducts = st.selectbox('Number of Products: ', (1,2,3,4), index=1)
        HasCrCard = st.selectbox('Credit Card Ownership: ', (0,1), index=1,help= '1 for have credit card, 0 for no creditcard')
        IsActiveMember = st.selectbox('Is active member : ', (0,1), index=1,help= '1 for active, 0 for passive member')
        EstimatedSalary = st.number_input('EstimatedSalary: ', min_value = 0,  value = 30000)

        #define submit button form
        submitted = st.form_submit_button('Predict')

    data_inf = {
    'Name' : name,
    'CreditScore' : CreditScore,
    'Geography' : geography,
    'Gender' : gender,
    'Age' : age,
    'Tenure' :tenure,
    'Balance': balance,
    'NumOfProducts' : numofproducts,
    'HasCrCard' :HasCrCard,
    'IsActiveMember' :IsActiveMember,
    'EstimatedSalary':EstimatedSalary,
    }
    data_inf = pd.DataFrame([data_inf])
    st.dataframe(data_inf)

    if submitted:
        
        #predict
        y_pred_inf = model.predict(data_inf)

        if y_pred_inf == 1:
            st.write('## Prediction Result : Churn')
        else:
            st.write('## Prediction Result : No Churn')

if __name__ == '__main__':
   run()