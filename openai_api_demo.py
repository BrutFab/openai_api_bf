import openai
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = API_KEY
print (API_KEY)


#Example 1 - print out availiable models you have access to
models = openai.Model.list()
available_models = [model.id for model in models["data"]]
print("Models available to you:")
for model in available_models:
    print(f"- {model}")


#Example 2 - example provided on the openai api documentation page
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ],
)

print (response['choices'][0]['message']['content'])

#Example 3 - example provided on the openai api documentation page
response_2 = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "write a 20-word poem about a robot"},
    ],
    temperature = 0,
)

print (response_2['choices'][0]['message']['content'])