import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image

# Load environment variables
load_dotenv()

# Configure Google API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_prompt, image):
    model = genai.GenerativeModel("gemini-1.5-pro-exp-0801")
    response = model.generate_content([input_prompt, image[0]])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Streamlit UI
st.set_page_config(page_title="Nutrition Analyzer", layout="wide")

st.title("🍽️ Nutrition Analyzer")
st.write("Upload an image of your meal to get a detailed nutritional analysis!")

col1, col2 = st.columns([1, 1])

with col1:
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

    analyze_button = st.button("Analyze Nutrition")

with col2:
    if uploaded_file is not None and analyze_button:
        with st.spinner("Analyzing your meal..."):
            image_data = input_image_setup(uploaded_file)
            
            input_prompt = """
            As a nutrition expert, analyze the food items in the image and provide a detailed nutritional breakdown. Please include:

            1. A list of identified food items with their estimated calorie content:
               - Item 1: [name] - [calories] kcal
               - Item 2: [name] - [calories] kcal
               (continue for all items)

            2. Total calorie estimate for the entire meal

            3. Macronutrient breakdown (percentage of total calories):
               - Carbohydrates: [x]%
               - Proteins: [x]%
               - Fats: [x]%

            4. Estimated fiber content (in grams)

            5. Estimated sugar content (in grams)

            6. Key vitamins and minerals present in significant amounts

            7. A brief assessment of the meal's nutritional balance:
               - Is it a well-balanced meal?
               - Are there any nutrients lacking?
               - Suggestions for improving the nutritional value, if applicable

            8. Any potential allergens or dietary restrictions to be aware of

            Please provide this information in a clear, easy-to-read format.
            """
            
            response = get_gemini_response(input_prompt, image_data)
            st.subheader("Nutritional Analysis")
            st.write(response)

st.sidebar.title("About")
st.sidebar.info(
    "This Nutrition Analyzer uses AI to provide detailed nutritional information "
    "about your meals. Simply upload an image of your food, and get insights about "
    "calories, macronutrients, and more!"
)
st.sidebar.title("Tips")
st.sidebar.markdown(
    """
    - Ensure the image clearly shows all food items
    - Include a variety of foods for a comprehensive analysis
    - The analysis is an estimate and should not replace professional dietary advice
    """
)