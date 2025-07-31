import streamlit as st
import time
import datetime
from pymongo import MongoClient
from openai import OpenAI

# Temporary:
question_bank = {
    'what is python': 'its a programming language',
    'what is streamlit': 'its a UI library for modern UI development in python',
    'can i build AI Agent': 'Yes, you can use Python, OpenAI, CrewAI and many more'
}

# Section1 - Security Configuration
# HW: Explore what is dotenv in python for securing your keys
MONGO_DB_URI = st.secrets['MONGO_DB_URI']
OPEN_AI_KEY = st.secrets['OPEN_AI_KEY']

# Section2 - Database Setup
client = MongoClient(MONGO_DB_URI)
db = client['gw2025']
patients_collection = db['aipatients']
consultations_collection = db['aiconsultations']

# Section3 - OpenAI Setup
openai_client = OpenAI(api_key=OPEN_AI_KEY)

# Section4 - Streamlit Page Configuration
st.set_page_config(page_title="Doctors AI Assistant")
st.title('Doctors AI Assistant App')

# Section5 - DB Helper Functions
def get_patient_by_phone(phone):
    return patients_collection.find_one(query={'phone':phone})

def add_patient(name, phone, email, gender, age, symptoms):    
    patient = get_patient_by_phone(phone)
    if patient:
        return 'Patient {} already available in the System with {}. Do you wish to write a consulstation ?'.format(name, phone)
    
    patient = {
                'name': name,
                'phone': phone,
                'email': email,
                'gender': gender,
                'age': age,
                'symptoms': symptoms,
                'created_on': datetime.datetime.now()
                }
    
    result = patients_collection.insert_one(patient)
    if result.inserted_id:
        return '{} added to the system with phone: {}'.format(name, phone)

def save_consultation(phone, medicines, remarks):
    consultation = {
                    'phone': phone,
                    'medicines': medicines,
                    'remarks': remarks
                    }
    result = consultations_collection.insert_one(consultation)
    if result.inserted_id:
        return ' consultation added to the system for phone: {}'.format(phone)
    
# Section6 - Streamlit Session State
if 'messages' not in st.session_state:
    st.session_state.messages = []
    
# Section7 - Print all the messages in the Session State (Chat History)
for message in st.session_state.messages:
    if message['role'] == 'user':    
        with st.chat_message(message['role']):
            st.markdown(message['content'])
    else:
        with st.chat_message(message['role']):
            st.markdown(message['content'])


# Section8 - Setup Open AI Function Tools
def ai_response(user_message):
    
    tools = [
                {
                    "type": "function",
                    "name": "add_patient",
                    "description": "Add a new patient in database",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"},
                            "phone": {"type": "string"},
                            "email": {"type": "string"},
                            "gender": {"type": "string"},
                            "age": {"type": "int"},
                            "symptoms": {"type": "string"}
                        },
                        "required": ["name", "phone", "email", "gender", "age"],
                    }
                },
                {
                    "type": "function",
                    "name": "save_consultation",
                    "description": "Add a new consultation of a ptient in database",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "phone": {"type": "string"},
                            "medicines": {"type": "string"},
                            "remarks": {"type": "string"},
                        },
                        "required": ["phone", "medicines"],
                }
            }

        ]
    
# Section9 - Streamlit Chat UI
user_input = st.chat_input('Type Your Question. Enter is Send..')
if user_input: # user_input if not None
    # st.markdown(user_input)
    message = {
        'role': 'user',
        'content': user_input
    }
    st.session_state.messages.append(message)
    with st.chat_message(message['role']):
        st.markdown(message['content'])

    if user_input in question_bank:
        message = {
            'role': 'ai',
            'content': question_bank[user_input]
        }
        st.session_state.messages.append(message)
        
        with st.chat_message(message['role']):
            typing_placeholder = st.empty()
            typing_text = ''
            for character in message['content']:
                typing_text += character
                typing_placeholder.markdown(typing_text)
                time.sleep(0.05)
    else:
        message = {
            'role': 'ai',
            'content': 'Sorry, I cannot answer this question'
        }
        st.session_state.messages.append(message)
        with st.chat_message(message['role']):
            typing_placeholder = st.empty()
            typing_text = ''
            for character in message['content']:
                typing_text += character
                typing_placeholder.markdown(typing_text)
                time.sleep(0.05)