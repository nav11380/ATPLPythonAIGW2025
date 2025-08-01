import streamlit as st
st.set_page_config(page_title='Health  Calculator')
st.title('All In One Health Calculator')

st.sidebar.header('Enter Your Details')
name = st.sidebar.text_input('Enter Your Name:')
age = st.sidebar.number_input('Enter Your Age:')
gender = st.sidebar.radio('Gender',options=['Male','Female'])
height = st.sidebar.number_input('Enter Your Height(cm):')
weight = st.sidebar.number_input('Enter Your Weight(kg):')

height = height/100
tab_list = ['BMI', 'BMR','Body Fat','Water Intake','Ideal Weight']
tab1, tab2, tab3, tab4, tab5 = st.tabs(tab_list)