from scorer import calculate_score

tests = [
    ("Python is interpreted language",
     "Python is interpreted language"),

    ("Python is interpreted language",
     "Python language"),

    ("Database stores data",
     "DB stores information"),

    ("Python programming language",
     "")
]

for i, (model, candidate) in enumerate(tests, start=1):

    score = calculate_score(model, candidate)

    print(f"\nTest Case {i}")
    print("Model Answer:", model)
    print("Candidate Answer:", candidate)
    print("Score:", score)