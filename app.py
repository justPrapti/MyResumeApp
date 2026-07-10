from flask import Flask, render_template,request
import joblib
import pdfplumber
import docx
import os

from skills import (
    extract_skills,
    calculate_ats,
    missing_skills,
    get_suggestions
)

app = Flask(__name__)

clf=joblib.load("model/clf.pkl")
tfidf=joblib.load("model/tfidf.pkl")
encoder=joblib.load("model/encoder.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])

def predict():

    file = request.files["resume"]
    filepath = os.path.join("uploads", file.filename)
    file.save(filepath)

    resume_text = extract_text(filepath)
    cleaned_resume = clean_resume(resume_text)


    resume_vector = tfidf.transform([cleaned_resume])

    prediction = clf.predict(resume_vector)

    category = encoder.inverse_transform(prediction)[0]

    print("Prediction:", prediction)
    print("Category:", category)
    print(type(category))

    detected_skills = extract_skills(cleaned_resume, category)

    ats_score = calculate_ats(category, detected_skills)

    missing = missing_skills(category, detected_skills)

    suggestions = get_suggestions(
        cleaned_resume,
        detected_skills,
        ats_score
    )

    score = abs(clf.decision_function(resume_vector).max())

    confidence = min(
        97,
        max(
            70,
            int(score * 18)
        )
    )

    return render_template(
        "result.html",
        filename=file.filename,
        category=category,
        confidence=confidence,
        skills=detected_skills,
        ats=ats_score,
        missing=missing,
        suggestions=suggestions
    )


def extract_text(filepath):
    text=""
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            page_text=page.extract_text()

            if page_text:
                text+=page_text+"\n"
    return text


import re
def clean_resume(text):
    text=text.lower()
    text=re.sub(r'http\S+|www\S+',' ',text)
    text=re.sub(r'[^\w\s]',' ',text)
    text=re.sub(r'\S+@\S+',' ',text)
    text=re.sub(r'\s+',' ',text).strip()
    return text


if __name__ == "__main__":
    app.run(debug=True)

