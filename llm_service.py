from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def generate_response(message: str):
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=message
    )

    return response.text