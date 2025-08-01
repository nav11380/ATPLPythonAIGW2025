from openai import OpenAI
def ai_response(user_message):
    tools = [
                {
                    "type": "function",
                    "name": "get_weather",
                    "description": "Get current temperature for a given location.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            
                        },
                        "required": [
                            "location"
                        ],
                        "additionalProperties": False
        }
}]
    
