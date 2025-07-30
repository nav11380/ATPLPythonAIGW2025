from Session26 import MongoDBHelper

db = MongoDBHelper()
# db.select_db(db_name='gw2025', collection='questionbank')
db.select_db(db_name='gw2025', collection='questions')

"""
question_bank = {

    '1': {
            'question':'what is python',
            'answer':'its a programming language',
            'keywords': ['python']
         },

    '2': {
            'question':'what is streamlit',
            'answer':'its a UI library for modern UI development in python',
            'keywords':['streamlit']
         },
    '3': {
            'question':'can i build AI Agent',
            'answer':'Yes, you can use Python, OpenAI, CrewAI and many more',
            'keywords': ['build', 'ai', 'agent']
         }, 
    '4': {
            'question':'which libraries can be used to build ai agent',
            'answer':'OpenAI, CrewAI, Hugging Face etc..',
            'keywords': ['build', 'libraries']
         },  
    '5': {
            'question':'how can i learn to code ai agent',
            'answer':'contact Ishant at 9915571177',
            'keywords': ['learn', 'code']
         },
}

result = db.insert(question_bank)
if result.inserted_id:
    print('Question Bank Created in MongoDB..')

"""

question_bank = [
    {
            'question':'what is python',
            'answer':'its a programming language',
            'keywords': ['python']
         },

    {
            'question':'what is streamlit',
            'answer':'its a UI library for modern UI development in python',
            'keywords':['streamlit']
         },
    {
            'question':'can i build AI Agent',
            'answer':'Yes, you can use Python, OpenAI, CrewAI and many more',
            'keywords': ['build', 'ai', 'agent']
         }, 
    {
            'question':'which libraries can be used to build ai agent',
            'answer':'OpenAI, CrewAI, Hugging Face etc..',
            'keywords': ['build', 'libraries']
         },  
    {
            'question':'how can i learn to code ai agent',
            'answer':'contact Ishant at 9915571177',
            'keywords': ['learn', 'code']
         }
    ]



for question in question_bank:
    result = db.insert(question)
    if result.inserted_id:
        print('Question Bank Created in MongoDB..')