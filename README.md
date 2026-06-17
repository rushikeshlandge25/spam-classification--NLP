# 📩 SMS Spam Detection using NLP & Naive Bayes

A machine learning project that classifies SMS messages as **Spam** or **Ham (Not Spam)** using Natural Language Processing techniques and the Multinomial Naive Bayes algorithm — trained with both **Bag of Words (BoW)** and **TF-IDF** feature extraction methods.

---

## 📌 Project Overview

This project builds a text classification model to automatically detect whether an SMS message is spam or legitimate (ham). Two feature extraction approaches — Bag of Words and TF-IDF — are compared using the same Naive Bayes classifier to observe the difference in performance.

---

## 📂 Dataset

- **File:** `spam.csv`
- **Columns Used:** `Message`, `Category`
- The `Category` column contains two labels: `spam` and `ham`
- The target variable is binary: **spam = 1**, **ham = 0**

---

## 🔧 Tech Stack

| Category | Tools / Libraries |
|---|---|
| Language | Python |
| Data Handling | Pandas, NumPy |
| NLP | NLTK (Stopwords, PorterStemmer), Regex |
| Feature Extraction | Scikit-learn (CountVectorizer, TfidfVectorizer) |
| ML Model | Scikit-learn (MultinomialNB) |
| Evaluation | Accuracy Score, Classification Report, Confusion Matrix |
| Environment | Jupyter Notebook |

---

## 🔄 Project Workflow

### 1. Data Loading
- Loaded `spam.csv` using Pandas
- Used `Message` as the input text and `Category` as the target label

### 2. Text Preprocessing
Built a custom cleaning pipeline for all messages:
- Removed **non-alphabetic characters** using Regex (`re.sub`)
- Converted text to **lowercase**
- Removed **English stopwords** using NLTK
- Applied **Porter Stemming** to reduce words to their root form
- Stored all cleaned messages in a `corpus` list

### 3. Label Encoding
- Used `pd.get_dummies()` on the `Category` column
- Extracted the `spam` column as binary target: **spam = 1, ham = 0**

---

## 🧪 Model 1 — Bag of Words (BoW) + Naive Bayes

- Applied **Binary CountVectorizer** with `max_features=2500` and `ngram_range=(1,2)` (unigrams + bigrams)
- Split data: **80% Train / 20% Test** (`random_state=0`)
- Trained **Multinomial Naive Bayes** on BoW features
- Evaluated using Accuracy Score and Classification Report

---

## 🧪 Model 2 — TF-IDF + Naive Bayes

- Applied **TfidfVectorizer** with `max_features=2500` and `ngram_range=(1,2)`
- Split data: **20% Train / 80% Test** (`random_state=42`)
- Trained **Multinomial Naive Bayes** on TF-IDF features
- Evaluated using Accuracy Score and Classification Report

> Both models use the same classifier to compare the impact of feature extraction method on performance.

---

## 📁 Project Structure

```
sms-spam-detection/
│
├── 1781670110509_model_trainer.ipynb   # Main Jupyter Notebook
├── spam.csv                            # Dataset (not included in repo)
└── README.md                           # Project documentation
```

---

## ▶️ How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/sms-spam-detection.git
   cd sms-spam-detection
   ```

2. Install required libraries:
   ```bash
   pip install pandas numpy scikit-learn nltk
   ```

3. Download NLTK resources (run once in Python):
   ```python
   import nltk
   nltk.download('stopwords')
   ```

4. Add `spam.csv` to the project folder.

5. Open and run the notebook:
   ```bash
   jupyter notebook 1781670110509_model_trainer.ipynb
   ```

---

## 📊 Results

Both models were evaluated on their respective test sets. Results including accuracy, precision, recall, and F1-score for spam and ham classes are available in the notebook output.

| Model | Feature Extraction | Vectorizer Settings |
|---|---|---|
| Model 1 | Bag of Words (Binary) | max_features=2500, ngram=(1,2) |
| Model 2 | TF-IDF | max_features=2500, ngram=(1,2) |

---

## 🙋 Author

**Rushi**
B.E. – Artificial Intelligence & Data Science
MET's Institute of Engineering, Nashik