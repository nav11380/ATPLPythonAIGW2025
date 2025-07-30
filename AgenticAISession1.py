"""
    Software Solution
    Model View Controller Architecture

    Agentic AI
    ( AI Model, Goal, and Task ) -> Controller
    ( Streamlit Chat UI ) -> View
    ( Any Data to be saved is dictionary ) -> Model

    Agentic AI with Python 
    Model is Dictionary Itself

    message = {
    'role': 'user',
    'content': 'what is python'
    }

    message = {
        'role': 'agent',
        'content': 'its a programming language'
    }

"""

import streamlit as st
import time
st.set_page_config(page_title='Chat UI')
st.title('Chat UI Demo1')
st.subheader('Ask a Question and i will help you with answer')

# Static QA -> I have written them in my program and it cannot grow or shrink
# Dynamic QA -> MongoDB
question_bank = {
    'what is python': 'its a programming language',
    'what is streamlit': 'its a UI library for modern UI development in python',
    'can i build AI Agent': 'Yes, you can use Python, OpenAI, CrewAI and many more'
}

# Create an empty list inside the session state of streamlit
# Session State is an Object's Reference, which will store the data temporarily
if 'messages' not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input('Type Your Question. Enter is Send..')
if user_input: # user_input if not None
    # st.markdown(user_input)
    message = {
        'role': 'user',
        'content': user_input
    }
    st.session_state.messages.append(message)

    if user_input in question_bank:
        message = {
            'role': 'ai',
            'content': question_bank[user_input]
        }
        st.session_state.messages.append(message)
    else:
        message = {
            'role': 'ai',
            'content': 'Sorry, I cannot answer this question'
        }
        st.session_state.messages.append(message)


for message in st.session_state.messages:
    if message['role'] == 'user':    
        with st.chat_message(message['role']):
            st.markdown(message['content'])
    else:
        with st.chat_message(message['role']):
            typing_placeholder = st.empty()
            typing_text = ''
            for character in message['content']:
                typing_text += character
                typing_placeholder.markdown(typing_text)
                time.sleep(0.05)

    
