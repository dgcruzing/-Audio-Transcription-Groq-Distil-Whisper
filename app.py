import streamlit as st
from openai import OpenAI
import os

# Set up the Streamlit app
st.title("Audio Transcription App")

# File uploader
uploaded_file = st.file_uploader("Choose an audio file", type=["mp3", "wav", "m4a"])

# API Key input
api_key = st.text_input("Enter your GROQ API Key", type="password")

if uploaded_file is not None and api_key:
    # Save the uploaded file temporarily
    with open("temp_audio.mp3", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Initialize OpenAI client
    client = OpenAI(api_key=api_key, base_url="https://api.groq.com/openai/v1")

    # Transcribe the audio
    if st.button("Transcribe Audio"):
        with st.spinner("Transcribing..."):
            with open("temp_audio.mp3", "rb") as audio_file:
                transcript = client.audio.transcriptions.create(
                    model="distil-whisper-large-v3-en",
                    file=audio_file,
                    response_format="text"
                )

        # Display the transcript
        st.subheader("Transcription:")
        st.write(transcript)

    # Clean up the temporary file
    os.remove("temp_audio.mp3")

else:
    st.write("Please upload an audio file and enter your API key to proceed.")