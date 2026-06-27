import json

import google.generativeai as genai

from config import GEMINI_API_KEY


genai.configure(
    api_key=GEMINI_API_KEY
)


model = genai.GenerativeModel(
    "gemini-2.5-flash"
)
async def classify_intent(text:str):


    prompt = f"""

You are an AI assistant classifier.

Classify this message.

Possible intents:

TASK
MEMORY
QUESTION
COMMAND
UNKNOWN


Message:

{text}


Return ONLY JSON:

{{
"intent":"",
"confidence":0.0
}}

"""


    response = model.generate_content(
        prompt
    )

    clean = (
    response.text
    .replace("```json", "")
    .replace("```", "")
    .strip()
)

    result = json.loads(clean)


    return result