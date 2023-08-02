import openai
import gradio as gr
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = API_KEY

def myGPT(message, history, system_prompt, tokens):
    chat_history = []
    for human, assistant in history:
        chat_history.append({"role": "user", "content": human })
        chat_history.append({"role": "assistant", "content":assistant})
    chat_history.append({"role": "user", "content": message})

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages= chat_history,         
        temperature=1.0, 
        stream = True,
    )
    #output = response['choices'][0]['message']['content']
    partial_message = ""
    for chunk in response:
        if len(chunk['choices'][0]['delta']) != 0:
            partial_message = partial_message + chunk['choices'][0]['delta']['content']
            yield partial_message

gr.ChatInterface(myGPT, 
                additional_inputs=[
                    gr.Textbox("You are helpful AI.", label="System Prompt"), 
                    gr.Slider(10, 100)
                ],
                title="BrutFab",
                description="Ask BrutFab any question",
                theme="soft", 
                examples=[["Hello"], ["Tell me about this app?"], ["What is api?"]],
                retry_btn=None,
                ).queue().launch(share=True)