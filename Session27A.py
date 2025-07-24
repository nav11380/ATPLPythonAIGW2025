"""
    Install ngrok
    execute below command for streamlit
    ngrok http 8501

    This will give you a URL, which can be used to 
    access your app from anywhere in the world

    bmi = weight / height**2
    
    Underweight: BMI less than 18.5. 
    Normal Weight: BMI between 18.5 and 24.9. 
    Overweight: BMI between 25 and 29.9. 
    Obese: BMI of 30 or higher. 

    Men: IBW (kg) = 48 + 2.7 * (height in centimeters - 152)
    Women: IBW (kg) = 45.5 + 2.2 * (height in centimeters - 152) 

    For Men: BMR = (10 x weight in kg) + (6.25 x height in cm) - (5 x age in years) + 5
    For Women: BMR = (10 x weight in kg) + (6.25 x height in cm) - (5 x age in years) - 161 

    For men, the formula is (1.20 x BMI) + (0.23 x Age) - 16.2
    For women, it is (1.20 x BMI) + (0.23 x Age) - 5.4

    Multiply your body weight in kilograms by 0.03, or 30 ml per kilogram

"""

import streamlit as st
from Session24 import MongoDBHelper

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
    bmi = 0
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
    if gender == 'Male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    
    st.subheader('Dear {}, Your BMR Calorie Per Day: {}'.format(name, bmr))
    
with tab3:
    st.subheader('Body Fat Percentage')
    if gender == 'Male':
        fat_percentage = round(1.20 * bmi + 0.23 * age - 16.2, 2)
    else:
        fat_percentage = round(1.20 * bmi + 0.23 * age - 5.4, 2)
    
    st.subheader('Dear {}, Your Body Fat Percentage is: {}'.format(name, fat_percentage))

with tab4:
    st.subheader('Water Intake')
    water_intake_litres = round(weight * 0.03, 2)
    st.subheader('Dear {}, Your Water Intake must be: {} lires'.format(name, water_intake_litres))


with tab5:
    st.subheader('Ideal Weight')
    height_inches = (height*100)/2.54
    if gender == 'Male':
        ideal_weight = 50 + 2.3 * (height_inches - 60)
    else:
        ideal_weight = 45.5 + 2.3 * (height_inches - 60)
    
    st.subheader('Dear {}, Your Ideal Weight must be: {} kgs'.format(name, round(ideal_weight, 2)))

    """
    db = MongoDBHelper()
    db.select_db(db_name='gw2025', collection='health')

    health_document = {
        'name': name,
        'age': age,
        'gender': gender,
        'height': height,
        'weight': weight,
        'bmi': bmi,
        'bmr': bmr,
        'fat': fat_percentage,
        'water': water_intake_litres,
        'ideal_weight': ideal_weight
    }

    result = db.insert(document=health_document)
    st.success('Document Added in Database with ID {}'.format(result.inserted_id))
    """
