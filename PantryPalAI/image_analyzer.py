from google import genai
from google.genai import types
from PIL import Image
from config import Config
from prompt_builder import build_ingredient_detection_prompt

def analyze_ingredients(image: Image.Image) -> list[str]:
    if not Config.GEMINI_API_KEY:
        raise ValueError("Gemini API Key is missing. Please check your .env file.")
        
    client = genai.Client(api_key=Config.GEMINI_API_KEY)
    
    prompt = build_ingredient_detection_prompt()
    
    try:
        response = client.models.generate_content(
            model=Config.MODEL_NAME,
            contents=[prompt, image],
            config=types.GenerateContentConfig(
                temperature=0.2,
            )
        )
        
        text = response.text.strip()
        if text.upper() == 'NONE':
            return []
            
        ingredients = [i.strip() for i in text.split(',')]
        return [i for i in ingredients if i]
    except Exception as e:
        raise RuntimeError(f"API Error during ingredient detection: {str(e)}")
