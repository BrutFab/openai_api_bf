import openai
import gradio as gr
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = API_KEY


def predict(message, history):
    history_openai_format = []
    for human, assistant in history:
        history_openai_format.append({"role": "user", "content": human })
        history_openai_format.append({"role": "assistant", "content":assistant})
    history_openai_format.append({"role": "user", "content": message})

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages= history_openai_format,         
        temperature=1.0,
        #stream=True
    )
    #print (response)
    partial_message = ""
    out = response['choices'][0]['message']['content']
    return out
    """for chunk in response:
        if len(chunk['choices'][0]['delta']) != 0:
            partial_message = partial_message + chunk['choices'][0]['delta']['content']
            yield partial_message """

#gr.ChatInterface(predict).queue().launch() 
gr.ChatInterface(predict).queue().launch() 