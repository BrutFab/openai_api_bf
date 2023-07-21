import requests
import openai
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = API_KEY
GPT_MODEL = "gpt-3.5-turbo"

endpoint = "https://api.openai.com/v1/chat/completions"

messages = []
messages.append({"role": "system", "content": "You are a helpful assistant."})
messages.append({"role": "user", "content": "which city in the US has the largest population?"})

json_data = {
    "model": GPT_MODEL,
    "messages": messages,
    "temperature": 0,
}

#headers
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + API_KEY,
}

response = requests.post(endpoint, headers=headers, json=json_data)
print(response.json()["choices"][0]["message"]["content"])
