import openai
import requests
from tenacity import retry, wait_random_exponential, stop_after_attempt
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = API_KEY

GPT_MODEL = "gpt-3.5-turbo"

@retry(wait=wait_random_exponential(multiplier=1, max=40), stop=stop_after_attempt(3))
def chat_completion_request(messages, model=GPT_MODEL):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + openai.api_key,
    }
    json_data = {"model": model, "messages": messages}
    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=json_data,
        )
        return response
    except Exception as e:
        print("Unable to generate ChatCompletion response")
        print(f"Exception: {e}")
        return e

messages = []
messages.append({"role": "system", "content": "You are a helpful assistant."})
messages.append({"role": "user", "content": "which city in the US has the largest population?"})
chat_response = chat_completion_request(messages)
assistant_message = chat_response.json()["choices"][0]["message"]
print(assistant_message)