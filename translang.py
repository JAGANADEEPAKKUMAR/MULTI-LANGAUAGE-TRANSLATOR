from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai


# ==============================
# Load environment variables
# ==============================
load_dotenv()

# You can store API key in .env instead (recommended)
# api_key = os.getenv("GOOGLE_API_KEY")

# Using directly (from your screenshot)
api_key = "AIzaSyD-o13DSoBV-G6mUatUvwYPQfnOlfs5jz0"
genai.configure(api_key=api_key)


# ==============================
# Function to translate text
# ==============================
def translate_text(text, source_language, target_language):
    MODEL_NAME = os.getenv("MODEL_NAME", "gemini-2.5-flash")
    model = genai.GenerativeModel(MODEL_NAME)


    prompt = (
        f"Translate the following text from {source_language} "
        f"to {target_language}: {text}"
    )

    response = model.generate_content([prompt])
    return response.text


# ==============================
# Initialize Streamlit app
# ==============================
st.set_page_config(
    page_title="AI-Powered Language Translator",
    page_icon="🌐"
)

st.header("🌐 AI-Powered Language Translator")


# ==============================
# User Inputs
# ==============================
text = st.text_area("📝 Enter text to translate:")

source_language = st.selectbox(
    "🌍 Select source language:",
    ["English", "Spanish", "French", "German", "Chinese","Telugu","Hindi"]
)

target_language = st.selectbox(
    "🌎 Select target language:",
    ["English", "Spanish", "French", "German", "Chinese","Telugu","Hindi"]
)


# ==============================
# Translate Button
# ==============================
if st.button("🔄 Translate"):

    if text and source_language and target_language:
        try:
            translated_text = translate_text(
                text,
                source_language,
                target_language
            )

            st.subheader("🗣 Translated Text:")
            st.write(translated_text)

        except Exception as e:
            st.error(f"⚠ Error: {str(e)}")

    else:
        st.warning("⚠ Please fill in all fields.")
