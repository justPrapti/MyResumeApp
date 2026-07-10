# AI Resume Screening System

An AI-powered Resume Screening System built using Machine Learning and Flask. The application analyzes uploaded resumes, predicts the most suitable job category, estimates an ATS score, identifies relevant skills, highlights missing skills, and provides improvement suggestions.

---

## Features

- Upload resumes in PDF format
- Automatic resume text extraction
- Resume preprocessing and cleaning
- Job category prediction using Machine Learning
- ATS score estimation
- Detected skills
- Missing skills analysis
- Resume improvement suggestions
- Clean and responsive Flask web interface

---

## Tech Stack

- Python
- Flask
- Scikit-learn
- TF-IDF Vectorizer
- Linear SVM (LinearSVC)
- Joblib
- pdfplumber
- HTML
- CSS

---

## Machine Learning Pipeline

Resume PDF

↓

Text Extraction

↓

Resume Cleaning

↓

TF-IDF Vectorization

↓

Linear SVM Classification

↓

Category Prediction

↓

ATS Score

↓

Skills Analysis

↓

Suggestions

---

## Project Structure

```
MyResumeApp/
│
├── app.py
├── skills.py
├── Resume.csv
├── requirements.txt
│
├── model/
│   ├── clf.pkl
│   ├── encoder.pkl
│   └── tfidf.pkl
│
├── static/
│   ├── style.css
│   └── result.css
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── uploads/
│
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/AI-Resume-Screening-System.git
```

Move into the project directory

```bash
cd AI-Resume-Screening-System
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## Model

- TF-IDF Vectorizer
- Linear Support Vector Machine (LinearSVC)

The model classifies resumes into multiple job categories based on the extracted resume text.

---

## Future Improvements

- Support DOCX resumes
- Job Description matching
- Resume ranking
- Resume keyword highlighting
- Transformer-based models (BERT)
- Cloud deployment

