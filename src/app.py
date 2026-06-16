from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel

from src.semantic_matcher import semantic_match
from src.matcher import analyze_skills
from src.extractor import extract_skills
from src.models import MatchResponse
from src.parser import extract_text_from_pdf
import tempfile

app = FastAPI()

class MatchRequest(BaseModel):
    cv_text: str
    job_text: str

@app.get("/")
def root():
    return {"message": "AI Job Matcher API is running"}

@app.post("/match")
def match(request: MatchRequest):
    score = semantic_match(
        request.cv_text,
        request.job_text
    )

    cv_skills = extract_skills(request.cv_text)
    job_skills = extract_skills(request.job_text)

    analysis = analyze_skills(cv_skills, job_skills)

    return MatchResponse(
        score = round(score * 100, 2),
        matching_skills = analysis["matching_skills"],
        missing_skills = analysis["missing_skills"]
    )

@app.post("/upload-cv")
async def upload_cv(
    file: UploadFile = File(...),
    job_text: str = ""
):
    # ideiglenes fájl mentése
    with tempfile.NamedTemporaryFile(delete = False, suffix = ".pdf") as tmp:
        content = await file.read()
        tmp.write(content)
        tmp_path = tmp.name
    
    # PDF -> text
    cv_text = extract_text_from_pdf(tmp_path)

    # matching
    score = semantic_match(cv_text, job_text)

    cv_skills = extract_skills(cv_text)
    job_skills = extract_skills(job_text)

    analysis = analyze_skills(cv_skills, job_skills)

    return {
        "score": round(score * 100, 2),
        "matching_skills": analysis["matching_skills"],
        "missing_skills": analysis["missing_skills"]
    }