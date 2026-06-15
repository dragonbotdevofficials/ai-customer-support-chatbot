import os
import google.generativeai as genai

api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.5-flash")
else:
    model = None


def ask_ai(prompt):
    if model is None:
        return "AI is not configured. Please add your Gemini API key."

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception:
        return "Sorry, I couldn't generate a response at the moment."
