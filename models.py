from typing import  List
from pydantic import BaseModel


class ChatGPTReq(BaseModel):
    messages: List
