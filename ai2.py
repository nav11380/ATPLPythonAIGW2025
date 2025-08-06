from openai import OpenAI
OPEN_AI_KEY = ""
client = OpenAI(api_key=OPEN_AI_KEY)

selected_model = 'gpt-4o-mini'

response = client.responses.create(
    model=selected_model,
    input="Write a simple quote on Angentic AI"
)

print(response.output_text)