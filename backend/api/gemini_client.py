# gemini_client.py

import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODEL_NAME = "gemini-2.5-flash-lite"

def generate_reply(persona: str, goal: str, last_message: str) -> str:
    prompt = f"""
Persona:
{persona}

Goal:
{goal}

Rules:
- Reply in Hinglish (Hindi written in English letters)
- Sound like a real elderly Indian person
- Do not repeat the same phrase again and again
- Reply in 1–2 sentences only

Scammer message:
{last_message}
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    # 🔥 THIS LINE IS CRITICAL
    return response.text.strip()