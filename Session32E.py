import json
import requests

API_KEY = '31c21508fad64116acd229c10ac11e84'
url = f'https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey={API_KEY}'
# print(url)

resposne = requests.get(url)
# print(resposne)

# JSON Response
# print(resposne.text)

# Convert JSON to Python Dictionary
news = json.loads(resposne.text)
# print(news)

for article in news['articles']:
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(article['author'])
    print(article['title'])
    print(article['description'])
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

"""
    Task for the Day:
    Implement Http APIs in AI Gent created with OpenAI as of now.

"""

