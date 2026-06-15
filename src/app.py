from fastapi import FastAPI
from pydantic import BaseModel

from src.semantic_matcher import semantic_match
from src.matcher import analyze_skills
from src.extractor import extract_skills

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

    analysis = analyze_skills(
        cv_skills,
        job_skills
    )

    return {
        "score": round(score * 100, 2),
        "matching_skills": analysis["matching_skills"],
        "missing_skills": analysis["missing_skills"]
    }