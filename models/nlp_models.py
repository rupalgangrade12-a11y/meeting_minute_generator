# import spacy
# from transformers import pipeline
# import nltk

# nltk.download("punkt")

# try:
#     nlp = spacy.load("en_core_web_sm")
# except:
#     import os
#     os.system("python -m spacy download en_core_web_sm")
#     nlp = spacy.load("en_core_web_sm")

# # Lightweight summarization model
# summarizer = pipeline(
#     "summarization",
#     model="sshleifer/distilbart-cnn-12-6"
# )

import spacy
from transformers import pipeline
import nltk

nltk.download("punkt")

nlp = spacy.load("en_core_web_sm")

summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6"
)