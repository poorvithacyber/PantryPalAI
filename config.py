import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    UPLOAD_DIR = "uploads"
    
    # Ensure upload directory exists
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    
    CUISINES = ["None", "Indian", "Italian", "Chinese", "Mexican"]
    DIETS = ["None", "High Protein", "Vegetarian", "Weight Loss"]
    
    MODEL_NAME = "gemini-flash-latest"
