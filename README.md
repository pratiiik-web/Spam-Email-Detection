# Spam Email Detection

Detect whether a message is spam or legitimate using
Natural Language Processing (NLP) and machine learning.

## Problem
Spam messages waste time and can be dangerous. This model
automatically classifies SMS messages as spam or ham (legitimate)
with 97% accuracy.

## Dataset
SMS Spam Collection — 5,572 messages (4,825 ham, 747 spam)
Source: Kaggle (uciml/sms-spam-collection-dataset)
Class split: 87% ham, 13% spam

## Key Findings
- Spam messages are nearly 2x longer than ham (139 vs 71 chars avg)
- Spam vocabulary: FREE, call, claim, won, prize, URGENT, txt, mobile
- Ham vocabulary: will, come, good, know, love, sorry, tomorrow
- Message length alone is a strong spam signal

## Results

| Model               | Accuracy | Spam Precision | Spam Recall |
|---------------------|----------|----------------|-------------|
| Naive Bayes         | 97%      | 99%            | 79%         |
| Logistic Regression | 96%      | 99%            | 73%         |

**Winner: Naive Bayes** — the classic algorithm for text classification,
originally designed for spam filtering.

## Why Precision Matters More Than Recall Here
A spam filter with high precision means legitimate emails
never go to the spam folder. Missing some spam is acceptable.
Sending real emails to spam is not. This model achieves 99%
spam precision — nearly zero false alarms.

## NLP Pipeline
Raw text → lowercase → remove punctuation/digits →
TF-IDF vectorization (3000 features) → Naive Bayes classifier

## How to Run
pip install -r requirements.txt
streamlit run apps/app.py

## Tech Stack
Python · Pandas · Scikit-learn · TF-IDF · Naive Bayes · Streamlit · WordCloud

## Project Structure
Spam Email Detection/
├── Data/
│   └── spam.csv
├── Models/
│   ├── model.pkl
│   └── tfidf.pkl
├── Notebooks/
│   └── 01_eda.ipynb
└── apps/
    └── app.py

## Key Lesson
NLP transforms raw text into numbers using TF-IDF.
Naive Bayes, despite being a simple algorithm, outperforms
Logistic Regression on text classification — proving that
the right algorithm for the problem beats the "fancier" one.# Spam Email Detection

Detect whether a message is spam or legitimate using
Natural Language Processing (NLP) and machine learning.

## Problem
Spam messages waste time and can be dangerous. This model
automatically classifies SMS messages as spam or ham (legitimate)
with 97% accuracy.

## Dataset
SMS Spam Collection — 5,572 messages (4,825 ham, 747 spam)
Source: Kaggle (uciml/sms-spam-collection-dataset)
Class split: 87% ham, 13% spam

## Key Findings
- Spam messages are nearly 2x longer than ham (139 vs 71 chars avg)
- Spam vocabulary: FREE, call, claim, won, prize, URGENT, txt, mobile
- Ham vocabulary: will, come, good, know, love, sorry, tomorrow
- Message length alone is a strong spam signal

## Results

| Model               | Accuracy | Spam Precision | Spam Recall |
|---------------------|----------|----------------|-------------|
| Naive Bayes         | 97%      | 99%            | 79%         |
| Logistic Regression | 96%      | 99%            | 73%         |

**Winner: Naive Bayes** — the classic algorithm for text classification,
originally designed for spam filtering.

## Why Precision Matters More Than Recall Here
A spam filter with high precision means legitimate emails
never go to the spam folder. Missing some spam is acceptable.
Sending real emails to spam is not. This model achieves 99%
spam precision — nearly zero false alarms.

## NLP Pipeline
Raw text → lowercase → remove punctuation/digits →
TF-IDF vectorization (3000 features) → Naive Bayes classifier

## How to Run
pip install -r requirements.txt
streamlit run apps/app.py

## Tech Stack
Python · Pandas · Scikit-learn · TF-IDF · Naive Bayes · Streamlit · WordCloud

## Project Structure
Spam Email Detection/
├── Data/
│   └── spam.csv
├── Models/
│   ├── model.pkl
│   └── tfidf.pkl
├── Notebooks/
│   └── 01_eda.ipynb
└── apps/
    └── app.py

## Key Lesson
NLP transforms raw text into numbers using TF-IDF.
Naive Bayes, despite being a simple algorithm, outperforms
Logistic Regression on text classification — proving that
the right algorithm for the problem beats the "fancier" one.
