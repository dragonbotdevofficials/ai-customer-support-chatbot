from fastapi import FastAPI
from pydantic import BaseModel
from ai_helper import ask_ai

app = FastAPI(title="AI Customer Support Chatbot API")


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "message": "AI Customer Support Chatbot API is running."
    }


@app.post("/chat")
def chat(request: ChatRequest):
    reply = ask_ai(request.message)
    return {
        "user_message": request.message,
        "bot_reply": reply
    }
