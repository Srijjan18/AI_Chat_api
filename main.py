from fastapi import FastAPI
from pydantic import BaseModel
from llm_service import generate_response
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def home():
    return FileResponse("static/index.html")

class ChatRequest(BaseModel):
    message : str


@app.post('/chat')
def chat_req(request : ChatRequest):
    try:
        answer = generate_response(request.message)
        return {'response' : answer}
    except Exception as e:
        print('Exception occurred: ',e)
        return {'response' : 'AI service is temporarily unavailable. Please try again later'}


@app.get('/models')
def models():
    return{
        "model": "gemini-3.6-flash",
        "provider": "Google Gemini"
    }