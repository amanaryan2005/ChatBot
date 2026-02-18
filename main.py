import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure API key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("API key not found. Please set GOOGLE_API_KEY in .env file.")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

st.title("🤖 Gemini Chatbot")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input:
        try:
            response = model.generate_content(user_input)
            st.session_state.history.append(("You", user_input))
            st.session_state.history.append(("Bot", response.text))
        except Exception as e:
            st.error(f"An error occurred: {e}")

for role, text in st.session_state.history:
    st.write(f"**{role}:** {text}")
