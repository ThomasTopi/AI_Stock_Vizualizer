import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_TOKEN"))

ai_model = genai.GenerativeModel(
    model_name = None,
    safety_settings= None,
    generation_config= None,
    system_instruction= None
)

#chat_seassion = ai_model.start_chat()