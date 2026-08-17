from google import genai
from google.genai import types
from config import Config
from prompt_builder import build_recipe_prompt

def generate_recipe(ingredients: list[str], cuisine: str, diet: str) -> str:
    if not Config.GEMINI_API_KEY:
        raise ValueError("Gemini API Key is missing. Please check your .env file.")
        
    if not ingredients:
        raise ValueError("No ingredients provided.")
        
    client = genai.Client(api_key=Config.GEMINI_API_KEY)
    
    prompt = build_recipe_prompt(ingredients, cuisine, diet)
    
    try:
        response = client.models.generate_content(
            model=Config.MODEL_NAME,
            contents=[prompt],
            config=types.GenerateContentConfig(
                temperature=0.7,
            )
        )
        return response.text
    except Exception as e:
        raise RuntimeError(f"API Error during recipe generation: {str(e)}")
