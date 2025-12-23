import spacy
from transformers import pipeline
import nltk

# Download NLTK data
nltk.download("punkt")
nltk.download("punkt_tab")

# Load SpaCy model safely
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    # Fallback (should not happen if requirements.txt is correct)
    import subprocess
    subprocess.run(
        ["python", "-m", "spacy", "download", "en_core_web_sm"],
        check=True
    )
    nlp = spacy.load("en_core_web_sm")

# Load summarization model
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)
