from nltk.tokenize import sent_tokenize

def extract_action_items(text):
    actions = []
    keywords = ["will", "should", "must", "by"]

    for sent in sent_tokenize(text):
        if any(word in sent.lower() for word in keywords):
            actions.append(sent)

    return actions
