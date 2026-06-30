from fastapi import FastAPI, UploadFile, File
from utils.pdf_reader import extract_text
from utils.text_cleaner import clean_text
from utils.skill_extractor import extract_skills


app = FastAPI()


@app.get("/")
def home():
    return {
        "message":"AI Resume Analyzer API Running"
    }


@app.post("/analyze")
def analyze_resume(file: UploadFile = File(...)):

    text = extract_text(file.file)

    clean = clean_text(text)

    skills = extract_skills(clean)


    return {
        "skills": skills,
        "text": clean
    }