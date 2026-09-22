def build_ingredient_detection_prompt() -> str:
    return (
        "Analyze this image and list the visible edible food ingredients. "
        "Ignore utensils, packaging, and background objects. "
        "Return a comma-separated list of ingredients. If no food is detected, return 'NONE'."
    )

def build_recipe_prompt(ingredients: list[str], cuisine: str, diet: str) -> str:
    cuisine_pref = f"Cuisine: {cuisine}." if cuisine != "None" else ""
    diet_pref = f"Diet preference: {diet}." if diet != "None" else ""
    
    ingredients_str = ", ".join(ingredients)
    
    prompt = f"""
    Create a recipe using mostly these detected ingredients: {ingredients_str}.
    {cuisine_pref}
    {diet_pref}
    
    You may add essential missing ingredients (like spices, oil, basic staples) but prioritize the detected ones. Do not hallucinate unavailable ingredients without listing them under 'Missing Ingredients'.
    
    Return the response in exactly this markdown format:
    
    # [Recipe Name]
    
    **Description:** [Short Description]
    
    **Detected Ingredients:**
    [List of detected ingredients used]
    
    **Missing Ingredients:**
    [List of missing ingredients needed]
    
    **Cooking Time:** [Time]
    **Preparation Time:** [Time]
    **Difficulty:** [Easy/Medium/Hard]
    **Number of Servings:** [Number]
    
    **Step-by-step Instructions:**
    1. [Step 1]
    2. [Step 2]
    ...
    
    **Tips:**
    - [Tip 1]
    - [Tip 2]
    """
    return prompt
