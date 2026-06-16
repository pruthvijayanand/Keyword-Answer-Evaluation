from keywords import extract_keywords

# Synonyms dictionary
synonyms = {
    "database": ["db"],
    "python": ["py"],
    "car": ["automobile"]
}

def keyword_match(keyword, candidate_keywords):

    # Exact match
    if keyword in candidate_keywords:
        return True

    # Synonym match
    if keyword in synonyms:
        for synonym in synonyms[keyword]:
            if synonym in candidate_keywords:
                return True

    return False


def calculate_score(model_answer, candidate_answer):

    if candidate_answer.strip() == "":
        return 0

    model_keywords = extract_keywords(model_answer)
    candidate_keywords = extract_keywords(candidate_answer)

    matches = 0

    for keyword in model_keywords:
        if keyword_match(keyword, candidate_keywords):
            matches += 1

    score = (matches / len(model_keywords)) * 10

    return round(score, 2)

def keyword_match(keyword, candidate_keywords):

    if keyword in candidate_keywords:
        return True

    if keyword in synonyms:
        for synonym in synonyms[keyword]:
            if synonym in candidate_keywords:
                return True

    return False
    for keyword in model_keywords:
        if keyword_match(keyword, candidate_keywords):
            matches += 1