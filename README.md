B6 - Keyword Based Answer Evaluation

Project Overview

This project implements a Keyword-Based Answer Evaluation System for automated assessment of descriptive answers. The system extracts important keywords from a model answer and compares them with keywords found in a candidate's response. Based on the number of matched keywords, a score is generated automatically.

The project is designed as part of the AI Assessment System and helps reduce manual evaluation effort while ensuring consistent scoring.

---

Features

- Keyword Extraction
- Stop Word Removal
- Keyword Matching
- Synonym Support
- Automatic Score Calculation
- JSON Output Format
- Multiple Test Case Validation

---

Project Structure

B6_Keyword_Evaluation/
│
├── main.py
├── keywords.py
├── scorer.py
├── test_cases.py
├── README.md
└── report.pdf

---

Technologies Used

- Python 3.x
- Visual Studio Code
- Regular Expressions (re)
- JSON

---

Methodology

Step 1: Input Collection

The system accepts:

- Model Answer
- Candidate Answer

Step 2: Keyword Extraction

Important keywords are extracted after removing stop words.

Example:

Model Answer:

Python is an interpreted programming language.

Extracted Keywords:

- python
- interpreted
- programming
- language

Step 3: Keyword Matching

Extracted keywords from the candidate answer are compared with model answer keywords.

Step 4: Synonym Matching

The system supports simple synonym mapping.

Example:

synonyms = {
    "database": ["db"],
    "python": ["py"],
    "car": ["automobile"]
}

Step 5: Score Calculation

Formula:

Score = (Matched Keywords / Total Keywords) × 10

---

Sample Input

Model Answer:

Python is an interpreted programming language.

Candidate Answer:

Python is a programming language.

---

Sample Output

{
    "score": 7.5
}

---

Test Cases

Test Case| Result
Perfect Match| 10.0
Partial Match| 6.67
Synonym Match| 6.67
Empty Answer| 0

---

Advantages

- Fast evaluation
- Consistent scoring
- Reduced manual effort
- Easy implementation
- Supports synonym matching

---

Limitations

- Depends on keywords
- Limited semantic understanding
- Does not fully understand answer context

---

Future Enhancements

- NLP-based keyword extraction
- Semantic similarity scoring
- Machine Learning integration
- FastAPI API deployment
- Detailed feedback generation

---

Conclusion

The Keyword-Based Answer Evaluation System successfully automates answer evaluation using keyword matching techniques. The project meets the requirements of Task B6 and serves as a foundation for advanced AI-powered assessment systems.