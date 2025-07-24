"""
    Install ngrok
    execute below command for streamlit
    ngrok http 8501

    This will give you a URL, which can be used to 
    access your app from anywhere in the world

"""

import streamlit as st
st.set_page_config(page_title='Health Calculator')
st.title('All In One Health Calculator')

st.sidebar.header('Enter Your Details')
name = st.sidebar.text_input('Enter Your Name: ')
age = st.sidebar.number_input('Enter Your Age: ', min_value=10, max_value=80)
gender = st.sidebar.radio('Gender', options=['Male', 'Female'])
height = st.sidebar.number_input('Enter Your Height (cm): ')
weight = st.sidebar.number_input('Enter Your Weight (in kgs): ')

# Later Convert Height to Meters
height = height/100

tab_list = ['BMI', 'BMR', 'Body Fat%', 'Water Intake', 'Ideal Weight']
tab1, tab2, tab3, tab4, tab5 = st.tabs(tab_list)

with tab1:
    st.subheader('Body Mass Index (BMI)')
    if height > 0 and weight > 0:
        bmi = round(weight / (height ** 2), 2)
        st.metric(label='BMI', value=bmi)
        if bmi < 18.5:
            st.warning('Hi {}, You are Underweight'.format(name))
        elif bmi > 18.5 and bmi < 24.9:
            st.success('Hi {}, You are Healthy with ideal weight'.format(name))
        elif bmi > 25 and bmi < 29.9:
            st.error('Hi {}, You are Overweight'.format(name))
        else:
            st.error('Hi {}, You are Obese'.format(name))

with tab2:
     st.subheader('Basal Metabolic Rate (BMR)')

with tab3:
    st.subheader('Body Mass Index (BMI)')

with tab4:
    st.subheader('Body Fat Percentage')

with tab5:
    st.subheader('Ideal Weight')