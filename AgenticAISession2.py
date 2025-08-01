"""
    How to use OPEN AI in Python Program
"""
from openai import OpenAI
OPEN_AI_KEY = ""
client = OpenAI(api_key=OPEN_AI_KEY)

selected_model = 'gpt-4o-mini'

response = client.responses.create(
    model=selected_model,
    input="Write a simple quote on Angentic AI"
)

print(response.output_text)
# Output:
"Agentic AI empowers us to unlock new possibilities, transforming ideas into action with intelligence and intent."
