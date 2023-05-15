import random
import gradio as gr
from langchain.memory import ChatMessageHistory
from langchain.chat_models import ChatOpenAI


history2 = ChatMessageHistory()

history2.add_user_message("hi robot!")
history2.add_ai_message("hi man!")



def chat(api_key, message, history):

    history = history or [('hi robot!', "hi man!")]
    print('api_key:', api_key)
    print('message:', message)
    print('history:', history)

    if (api_key==""):
        return "请在api_key输入您的GPT api key。", history, history
    chat = ChatOpenAI(temperature=0, openai_api_key=api_key)

    if (message==""):
        return "请在message输入您的对话消息。", history, history

    message = message.lower()
    
    print('29')
    history2.add_user_message(message)
    ai_response = chat(history2.messages)
    print('32')
    
    history2.add_ai_message(ai_response.content)
    response = ai_response.content
    
    history.append((message, response))
    return "智能对话机器人正在与您进行对话。", history, history
    
    
chatbot = gr.Chatbot().style(color_map=("green", "pink"))

demo = gr.Interface(
    chat,
    ["text", "text", "state"],
    ["text", chatbot, "state"],
)

demo.launch()
