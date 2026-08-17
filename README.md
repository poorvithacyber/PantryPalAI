# PantryPal AI 🍳

"Turn Your Ingredients into Delicious Recipes with AI."

## Overview
PantryPal AI is a modern AI-powered web application that allows users to upload an image of pantry ingredients and generates personalized recipes based on selected cuisine and diet preferences. It utilizes Google's Gemini multimodal capabilities to detect ingredients and craft delicious meals.

## Features
- **Image Analysis**: Upload an image and Gemini Vision detects the visible food ingredients.
- **Recipe Generation**: Generates complete recipes based on detected ingredients.
- **Customization**: Choose your preferred cuisine (Indian, Italian, Chinese, Mexican) and diet preference (High Protein, Vegetarian, Weight Loss).
- **Beautiful UI**: Modern and responsive interface built with Streamlit.

## Architecture
- **Frontend**: Streamlit
- **AI/LLM**: Google Gemini API (`gemini-2.5-flash`)
- **Language**: Python

## Folder Structure
```
PantryPalAI/
├── app.py                  # Main Streamlit application
├── recipe_generator.py     # Gemini text generation logic
├── image_analyzer.py       # Gemini vision logic
├── prompt_builder.py       # Prompt engineering
├── config.py               # Configuration and constants
├── utils.py                # Helper functions
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── .env.example            # Environment variables template
├── .gitignore              # Git ignore file
├── assets/                 # Static assets (images, logos)
├── uploads/                # Directory for uploaded user images
└── screenshots/            # UI screenshots
```

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/PantryPalAI.git
   cd PantryPalAI
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables:**
   - Copy `.env.example` to a new file named `.env`.
   - Add your Google Gemini API key to `.env`:
     ```
     GEMINI_API_KEY=your_gemini_api_key_here
     ```

## How to Run

Execute the following command in the project root:
```bash
streamlit run app.py
```
Then, open the provided local URL in your web browser.

## Screenshots

*(Placeholder for screenshots of the application)*

## Future Improvements
- Multi-image support for larger pantries.
- Recipe saving and sharing functionality.
- Nutritional breakdown of generated recipes.
- Integration with grocery delivery APIs for missing ingredients.
