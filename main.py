import os
import openai
from fastapi import FastAPI

from models import ChatGPTReq


app = FastAPI()
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY


@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.post("/chatgpt")
async def chatgpt(req: ChatGPTReq):
    """
    请求格式：
    {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "I need help."},
            {"role": "assistant", "content": "How can I help you?"},
            ...
        ]
    }
    """
    return openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=req.messages
    )
