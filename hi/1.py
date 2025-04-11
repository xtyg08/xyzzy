
import streamlit as st
import os
import google.generativeai as genai
from google.generativeai import GenerativeModel

# 🌸 Streamlit Page Config
st.set_page_config(page_title="From Me to You 💕", page_icon="💬", layout="centered")

# 🌈 Cute Styling
st.markdown("""
    <style>
    body {
        background-color: #fff0f5;
    }
    .stButton > button {
        background-color: #ff69b4;
        color: white;
        font-weight: bold;
        border-radius: 15px;
        padding: 10px 20px;
    }
    .stTextInput>div>div>input {
        background-color: #ffe6f0;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 🔐 Load Gemini API Key from Streamlit Secrets
api_key = os.getenv("AIzaSyBLX4z7jttqwBoo8AnNudqlzyb2gR5ifS0")

if not api_key:
    st.error("API key not found. Please set GEMINI_API_KEY in your environment or Streamlit secrets.")
    st.stop()

# 🤖 Configure Gemini
genai.configure(api_key=api_key)
model = GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

# 🧡 App Title
st.title("💬 From Me to You")
st.write("Hey love, it’s me... your favorite human. Type anything here — I’m always listening. 💗")

# 💬 Chat Input
user_input = st.text_input("Type here, baby...")

if st.button("Send 💌"):
    if user_input:
        prompt = f"""
        You are acting as a very loving, romantic boyfriend talking to his girlfriend.
        Speak in a heartfelt, warm, sweet, and sometimes playful tone.
        Use nicknames like baby, sweetheart, cutie, my love, etc.
        You miss her, love her deeply, and want to make her smile.

        Here's what she said: "{user_input}"
        Reply as her boyfriend would in a sweet, thoughtful, romantic way.
        """

        response = chat.send_message(prompt)
        st.markdown(f"**You:** {response.text}")
    else:
        st.warning("Type something, babe!")
