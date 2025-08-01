"""
    Response from OPEN AI for Chat Completion is a Choice
    [Doctors Assistant AI App] choice: 
    Choice(finish_reason='tool_calls', index=0, 
    logprobs=None, message=ChatCompletionMessage(content=None, refusal=None, 
    role='assistant', annotations=[], audio=None, function_call=None, 
    tool_calls=[ChatCompletionMessageToolCall(id='call_lwS7x5WKSRv3c3SMKv0qk4cK', 
    function=Function(arguments='{"name":"Sia","phone":"987650987",
    "email":"sia@example.com","gender":"female","age":28,
    "symptoms":"high fever with stomach ache"}', 
    name='add_patient'), type='function')]))

"""

import streamlit as st
import time
import datetime
from pymongo import MongoClient
from openai import OpenAI
import json

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
selected_model = 'gpt-4o-mini'

# Section4 - Streamlit Page Configuration
st.set_page_config(page_title="Doctors AI Assistant")
st.title('Doctors AI Assistant App')

# Section5 - DB Helper Functions
def get_patient_by_phone(phone):
    # find_one is MongoDB built in function
    return patients_collection.find_one({'phone':phone})

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
    # insert_one belongs to MongoDB
    result = patients_collection.insert_one(patient)
    if result.inserted_id:
        return '{} added to the system with phone: {}'.format(name, phone)

def save_consultation(phone, medicines, remarks):
    consultation = {
                    'phone': phone,
                    'medicines': medicines,
                    'remarks': remarks,
                    'created_on': datetime.datetime.now()
                    }
    result = consultations_collection.insert_one(consultation)
    if result.inserted_id:
        return ' consultation added to the system for phone: {}'.format(phone)

def fetch_all_patients():
    pass

def fetch_all_consultations():
    pass

# Section6 - Streamlit Session State
# over here, the list of messages is temporary
# this list can also be used to save the data in a file (offline)
# this list can also be used to save the data in mongo db (online)
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
def ai_response(user_input):
    
    tools = [
                {
                    "type": "function",
                    "function":{
                        "name": "add_patient",
                        "description": "Add a new patient in database",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "name": {"type": "string"},
                                "phone": {"type": "string"},
                                "email": {"type": "string"},
                                "gender": {"type": "string"},
                                "age": {"type": "number"},
                                "symptoms": {"type": "string"}
                            },
                            "required": ["name", "phone", "email", "gender", "age"],
                        }
                    }
                },
                {
                    "type": "function",
                    "function":{
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
            }

        ]
    
    response = openai_client.chat.completions.create(
        model=selected_model,
        messages=[
            # this is role as doctors assistant
            {'role': 'system', 'content': 'You are a doctors assistant. Use phone number as unique key and write medicines as well if required.'},
            # this is the previous chat context which we are also sending alongwith
            *[{'role': message['role'], 'content': message['content']} for message in st.session_state.messages],
            # immediate user question/prompt/input
            {'role': 'user', 'content': user_input}
        ],
        tools=tools
    )

    print('[Doctors Assistant AI App] response:', response)
    choice = response.choices[0]
    print('[Doctors Assistant AI App] choice:', choice)
    
    if choice.finish_reason == 'tool_calls':
        function_name = choice.message.tool_calls[0].function.name
        arguments = choice.message.tool_calls[0].function.arguments
        # JSON to Dictionary
        # i.e. string representation of dicionary which is JSON
        # to python dictionary
        arguments = json.loads(arguments)
        # json.dumps -> convert python dictionary into JSON
        if function_name == 'add_patient':
            return add_patient(**arguments)
        elif function_name == 'save_consultation':
            return save_consultation(**arguments)
    else:
        return "I cannot process your input. please try agian !"
    
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

    message = {
        'role': 'assistant',
        'content': ai_response(user_input)
    }
    st.session_state.messages.append(message)
        
    with st.chat_message(message['role']):
        typing_placeholder = st.empty()
        typing_text = ''
        for character in message['content']:
            typing_text += character
            typing_placeholder.markdown(typing_text)
            time.sleep(0.03)