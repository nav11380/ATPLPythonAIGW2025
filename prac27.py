import streamlit as st

st.title('BMI Calculator')

col1,col2 = st.column(2)










with col1:
    name = st.text_input('Enter Your Name:')
    height = st.number_input('Enter Your Height(meters):')
    weight = st.number_input('Enter Your Weight(kgs):')

with col2:
    if height > 0 and weight > 0:
        bmi  = round(weight/ (height ** 2),2)
        st.metric(label = 'BMI',value = bmi)

        if bmi < 18.5:
            st.warning ('Hi {}, You are Underweight'.format(name))
