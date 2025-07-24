"""
    Gain HandsOn -> Read and Learn from Documentation
    https://streamlit.io/

    bmi = weight / height**2
    
    Underweight: BMI less than 18.5. 
    Normal Weight: BMI between 18.5 and 24.9. 
    Overweight: BMI between 25 and 29.9. 
    Obese: BMI of 30 or higher. 

    command to execute streamlit app
    streamlit run Session27.py

"""
import streamlit as st

st.title('BMI Calculator')

col1, col2 = st.columns(2) # it will retunr number of column objects as mentioned

with col1:
    name = st.text_input('Enter Your Name: ')
    height = st.number_input('Enter Your Height (meters): ')
    weight = st.number_input('Enter Your Weight (in kgs): ')

with col2:
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
        

