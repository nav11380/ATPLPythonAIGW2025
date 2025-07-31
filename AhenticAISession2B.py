# Function tool - Documentation 
# https://platform.openai.com/docs/guides/function-calling?api-mode=responses

from openai import OpenAI

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
    
    OPEN_AI_KEY = ""
    client = OpenAI(api_key=OPEN_AI_KEY)
    selected_model = 'gpt-4o-mini'

    response = client.chat.completions.create(
        model=selected_model,
        input=[
                {"role": "system", "content": "You are a Doctors Agent who can create patients and save consultations"},
                {"role": "user", "content": user_message}
            ],
        tools=tools
    )
