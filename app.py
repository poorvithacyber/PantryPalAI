import streamlit as st
from PIL import Image
import os
from config import Config
from image_analyzer import analyze_ingredients
from recipe_generator import generate_recipe
from utils import show_error, show_warning

st.set_page_config(
    page_title="PantryPal AI",
    page_icon="🍳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar
with st.sidebar:
    st.title("🍳 PantryPal AI")
    st.markdown("Turn Your Ingredients into Delicious Recipes with AI.")
    
    st.header("Preferences")
    cuisine = st.selectbox("Cuisine", Config.CUISINES)
    diet = st.selectbox("Diet Preference", Config.DIETS)
    
    st.markdown("---")
    st.markdown("### About")
    st.info(
        "Upload an image of your pantry or ingredients, "
        "and let Gemini AI craft a personalized recipe for you."
    )

# Main Page
st.title("Welcome to PantryPal AI")
st.markdown("Upload a photo of your ingredients to get started.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Save the uploaded file
    file_path = os.path.join(Config.UPLOAD_DIR, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
        
    image = Image.open(uploaded_file)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.image(image, caption="Uploaded Ingredients", use_container_width=True)
        
    with col2:
        if st.button("Analyze Ingredients", type="primary"):
            with st.spinner("Analyzing image..."):
                try:
                    ingredients = analyze_ingredients(image)
                    if not ingredients:
                        show_warning("No food ingredients detected in the image.")
                        st.session_state.ingredients = []
                    else:
                        st.session_state.ingredients = ingredients
                        st.success("Analysis complete!")
                except Exception as e:
                    show_error(str(e))
                    st.session_state.ingredients = []
                    
        if 'ingredients' in st.session_state and st.session_state.ingredients:
            st.subheader("Detected Ingredients")
            # Display ingredients nicely
            ingredients_html = "".join([f"<span style='background-color:#f0f2f6; padding:5px 10px; border-radius:15px; margin:5px; display:inline-block; color:black;'>{ing}</span>" for ing in st.session_state.ingredients])
            st.markdown(ingredients_html, unsafe_allow_html=True)
            
            st.markdown("---")
            if st.button("Generate Recipe 🪄", type="primary"):
                with st.spinner("Chef Gemini is crafting your recipe..."):
                    try:
                        recipe = generate_recipe(st.session_state.ingredients, cuisine, diet)
                        st.session_state.recipe = recipe
                    except Exception as e:
                        show_error(str(e))
                        
if 'recipe' in st.session_state and st.session_state.recipe:
    st.markdown("---")
    st.markdown(st.session_state.recipe)
