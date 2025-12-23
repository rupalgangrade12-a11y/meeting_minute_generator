import speech_recognition as sr
import tempfile
import os

def transcribe_audio(uploaded_file):
    recognizer = sr.Recognizer()

    # Tuning for better recognition
    recognizer.energy_threshold = 200
    recognizer.dynamic_energy_threshold = True
    recognizer.pause_threshold = 1.0
    recognizer.non_speaking_duration = 0.5

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp:
        temp.write(uploaded_file.read())
        temp_path = temp.name

    try:
        with sr.AudioFile(temp_path) as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio_data = recognizer.record(source)

        text = recognizer.recognize_google(
            audio_data,
            language="en-IN",   # Indian English
            show_all=False
        )

    except sr.UnknownValueError:
        text = (
            "Audio not clear enough. "
            "Please speak slowly and clearly with pauses."
        )

    except sr.RequestError:
        text = "Speech recognition service unavailable. Check internet."

    os.remove(temp_path)
    return text
