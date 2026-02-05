import os
from dotenv import load_dotenv
import google.generativeai as genai


load_dotenv()

MODEL_NAME = "gemini-2.5-flash-lite"

class GeminiClient:
    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel(MODEL_NAME)

    def generate(self, prompt):
        response = self.model.generate_content(prompt)
        return response.text


def generate_reply(persona: str, goal: str, scammer_message: str) -> str:
    client = GeminiClient()

    prompt = f"""
Persona: {persona}
Goal: {goal}

Scammer said:
{scammer_message}

Respond like the persona while trying to waste scammer time.
"""

    return client.generate(prompt)
