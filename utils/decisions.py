from nltk.tokenize import sent_tokenize

def extract_decisions(text):
    decisions = []
    patterns = ["decided", "approved", "agreed", "finalized"]

    for sent in sent_tokenize(text):
        if any(p in sent.lower() for p in patterns):
            decisions.append(sent)

    return decisions
