from AgenticAISession1B import get_questions
import streamlit as st
import time

# Dynamic Question Bank
question_bank = get_questions()

def find_answer(question):
    
    # Your logic1 goes here which you will find in question_bank list
    # Your logic2 goes here which you will find in questions collection of mongodb list
    # answer = ''
    # return answer

    return None

def find_answer_from_db(question):
    
    # Your logic2 goes here which you will find in questions collection of mongodb list
    # answer = ''
    # return answer

    return None


st.set_page_config(page_title='Chat UI')
st.title('Chat UI Demo1')
st.subheader('Ask a Question and i will help you with answer')

# Create an empty list inside the session state of streamlit
# Session State is an Object's Reference, which will store the data temporarily
if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    if message['role'] == 'user':    
        with st.chat_message(message['role']):
            st.markdown(message['content'])
    else:
        with st.chat_message(message['role']):
            st.markdown(message['content'])

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

    answer = find_answer(user_input)

    if answer:
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

    
