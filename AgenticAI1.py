import streamlit as st
import time
st.set_page_config(page_title='Chat UI')
st.title('Chat UI Demo')
st.subheader('Ask a question and i will answer')

question_bank = {
    'what is python' : 'its a programming language',
    'what is streamlit' : 'its a ui library for modern UI development in python',
    'can i build AI Agent' : 'Yes,you can use Python ,open AI,Crew AI and many more'
    }

#st.markdown('This is a markdown')
'''message = {
    'role' : 'user',
    'content' : 'what is python'
}'''


if 'messages' not in st.session_state:
    st.session_state.messages =[]

for message in st.session_state.messages:
    if message['role'] == 'user':    
        with st.chat_message(message['role']):
            st.markdown(message['content'])
    else:
        with st.chat_message(message['role']):
            st.markdown(message['content'])

#for message in st.session_state.messages:
 #   st.markdown('{role}\{content}'.format_map(message))

user_input = st.chat_input('Type your Question.Enter is send..')
if user_input:
    #st.markdown(user_input)
    message = {
        'role' : 'user',
        'content' : user_input
    }
    st.session_state.messages.append(message)
    with st.chat_message(message['role']):
        st.markdown(message['content'])

    if user_input in question_bank:
        message ={
            'role' :'ai',
            'content' : question_bank[user_input]
        }
        st.session_state.messages.append(message)

        with st.chat_message(message['role']):
            typing_placeholder = st.empty()
            typing_text = ''
            for character in message['content']:
                typing_text += character
                typing_placeholder.markdown(typing_text)
                time.sleep(0.05)
    else :
        message= {
            'role' : 'ai',
            'content' : 'Sorry, i cannot answer this question'
        }
        st.session_state.messages.append(message)
        with st.chat_message(message['role']):
            typing_placeholder = st.empty()
            typing_text = ''
            for character in message['content']:
                typing_text += character
                typing_placeholder.markdown(typing_text)
                time.sleep(0.05)





