from models.nlp_models import summarizer

def generate_summary(text):
    if len(text.split()) < 50:
        return text

    summary = summarizer(
        text,
        max_length=150,
        min_length=60,
        do_sample=False
    )
    return summary[0]["summary_text"]
