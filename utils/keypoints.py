from models.nlp_models import nlp

def extract_key_points(text):
    doc = nlp(text)
    points = []

    for sent in doc.sents:
        if len(sent.text.split()) > 6:
            points.append(sent.text)

    return points[:5]
