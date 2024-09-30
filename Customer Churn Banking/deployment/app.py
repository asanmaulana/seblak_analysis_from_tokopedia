import streamlit as st
import eda
import prediction

page = st.sidebar.selectbox('Choose The Page: ', ('EDA', 'Model Prediction'))

if page == 'EDA':
    eda.run()
else:
    prediction.run()