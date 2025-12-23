from models.nlp_models import nlp

def identify_speakers(text):
    speaker_data = []

    doc = nlp(text)

    for sent in doc.sents:
        persons = [ent.text for ent in sent.ents if ent.label_ == "PERSON"]

        if persons:
            for person in persons:
                speaker_data.append({
                    "speaker": person,
                    "statement": sent.text
                })

    return speaker_data
