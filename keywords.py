import re

def extract_keywords(text):

    stop_words = {
        "is","a","an","the","and","or",
        "to","of","for","in","on"
    }

    words = re.findall(r'\b\w+\b', text.lower())

    keywords = [
        word for word in words
        if word not in stop_words
    ]

    return list(set(keywords))