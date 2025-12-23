import spacy
from transformers import pipeline
import nltk

nltk.download("punkt")
nltk.download("punkt_tab")

nlp = spacy.load("en_core_web_sm")

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)
