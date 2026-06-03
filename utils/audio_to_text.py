import speech_recognition as sr
from pydub import AudioSegment
import tempfile
import os

def transcribe_audio(uploaded_file):

    # Create temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        temp_path = temp_audio.name

    # Convert uploaded audio to WAV
    audio = AudioSegment.from_file(uploaded_file)
    audio.export(temp_path, format="wav")

    recognizer = sr.Recognizer()

    with sr.AudioFile(temp_path) as source:
        audio_data = recognizer.record(source)

    text = recognizer.recognize_google(audio_data)

    # Delete temp file
    os.remove(temp_path)

    return text