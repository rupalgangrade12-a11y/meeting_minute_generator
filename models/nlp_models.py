import spacy
from transformers import pipeline
import nltk

nltk.download("punkt")

nlp = spacy.load("en_core_web_sm")

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)