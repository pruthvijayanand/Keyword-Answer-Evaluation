import json
from scorer import calculate_score

model_answer = """
Python is an interpreted programming language.
"""

candidate_answer = """
Python is a programming language.
"""

score = calculate_score(
    model_answer,
    candidate_answer
)

result = {
    "score": score
}

print(json.dumps(result, indent=4))