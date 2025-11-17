from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class Message(BaseModel):
    text: str

# Simple placeholder AI response for now
def fake_ai_reply(user_text: str):
    responses = [
        "Nimekusikia. Hebu nieleze zaidi...",
        "Ahsante kwa swali. Hii ni toleo la mfano la Safari AI.",
        "Niko hapa kukusaidia. Unaweza kuuliza swali lingine?",
        "Safari AI (demo): bado tunajifunza kutoka kwa data ya Kiswahili."
    ]
    return random.choice(responses)

@app.post("/chat")
def chat(message: Message):
    response = fake_ai_reply(message.text)
    return {"reply": response}
