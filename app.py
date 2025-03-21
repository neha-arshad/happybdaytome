import streamlit as st
import time
import base64
import urllib.parse
import os
from PIL import Image

# Title
st.title("🎉 Happy Birthday TO Me! 🎂")

# Birthday Message
st.write("## Wishing Myself a Very Happy Birthday! 🎈")

# Function to Load Animated GIF
def get_base64_of_gif(file_path):
    try:
        with open(file_path, "rb") as gif_file:
            contents = gif_file.read()
        return base64.b64encode(contents).decode("utf-8")
    except FileNotFoundError:
        st.error("⚠️ GIF file not found! Please check the file path.")
        return None

def display_gif(gif_path):
    gif_base64 = get_base64_of_gif(gif_path)
    if gif_base64:
        gif_html = f'<img src="data:image/gif;base64,{gif_base64}" width="100%">'
        st.markdown(gif_html, unsafe_allow_html=True)

if st.button("Celebrate 🎉"):
    st.write("### Yay! It's My Special Day! 🥳")
    
    # Simulate loading effect
    with st.spinner("Getting everything ready..."):
        time.sleep(2)
    
    # Display Animated Cake GIF
    display_gif("birthday-to-me.gif")  # Ensure this file is in your project directory
    
    st.balloons()

# Function to Load and Encode Audio File
def get_audio_base64(file_path):
    try:
        with open(file_path, "rb") as f:
            audio_bytes = f.read()
        return base64.b64encode(audio_bytes).decode()
    except FileNotFoundError:
        return None

# Local MP3 File Path
mp3_file_path = "birthdaysong.mp3"

if os.path.exists(mp3_file_path):  # Checking if file exists
    audio_base64 = get_audio_base64(mp3_file_path)
    if audio_base64:
        music_html = f"""
        <audio autoplay loop>
            <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
            Your browser does not support the audio element.
        </audio>
        """
        st.markdown(music_html, unsafe_allow_html=True)
else:
    st.error("⚠️ Background music file not found! Please check the file path.")

# Special Birthday Note
st.markdown("**Today is my day to shine! Wishing myself happiness, success, and endless joy! ✨**")

# Share Button with URL Encoding
share_text = "It's my Birthday! 🎂 Celebrate with me! 🥳"
encoded_text = urllib.parse.quote(share_text)  # URL encoding

whatsapp_url = f"https://api.whatsapp.com/send?text={encoded_text}"
st.markdown(f"[Share on WhatsApp]({whatsapp_url})")
