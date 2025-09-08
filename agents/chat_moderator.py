import google.generativeai as genai
import os
import json
from dotenv import load_dotenv
from utils.validator import contains_phone_number

# ✅ Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing in .env file")

# ✅ Configure Gemini API
genai.configure(api_key=api_key)

# ✅ Use Gemini 2.0 Flash model
model = genai.GenerativeModel("gemini-2.0-flash")

def moderate_chat(message: str) -> dict:
    """
    Classify the message and return JSON with status and reason.
    Example:
    {
        "status": "Abusive",
        "reason": "Contains insulting language"
    }
    """

    # ✅ First check for phone number locally
    if contains_phone_number(message):
        return {
            "status": "Contains Phone Number",
            "reason": "Message includes a 10-digit phone number"
        }

    # ✅ Ask Gemini for JSON classification
    prompt = f"""
    You are a chat moderation system for a marketplace.
    Classify the message into one of these categories:
    - Safe
    - Abusive
    - Spam

    Also provide a reason for your classification.

    Respond ONLY in JSON format like this:
    {{
        "status": "<category>",
        "reason": "<reason for classification>"
    }}

    Message: "{message}"
    """

    response = model.generate_content(prompt)

    try:
        return json.loads(response.text)
    except:
        # If parsing fails, return fallback
        return {
            "status": "Unknown",
            "reason": response.text.strip()
        }
