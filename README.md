## -Audio-Transcription-Groq-Distil-Whisper

Audio Transcription Local run using Streamlit App

### Create a new directory for your project (optional)

mkdir streamlit-transcription-app

cd streamlit-transcription-app

### Create a virtual environment

python -m venv venv

## Activate the virtual environment

### On Windows:

venv\Scripts\activate

### On macOS and Linux:

#source venv/bin/activate

### Install required packages

pip install streamlit openai

### Create a new file for your Streamlit app
### You can use your preferred text editor to create and edit this file
### For example, using the 'type' command on Windows or 'touch' on macOS/Linux:

### Windows:
type nul > app.py

### macOS/Linux:

touch app.py

### Now, open app.py in your text editor and paste the Streamlit app code

### Run the Streamlit app

streamlit run app.py

### When you're done, deactivate the virtual environment

deactivate
