from src.parser import extract_text_from_pdf
from src.extractor import extract_skills
from src.semantic_matcher import semantic_match

def run_pipeline(cv_path: str, job_text: str):
    cv_text = extract_text_from_pdf(cv_path)

    cv_skills = extract_skills(cv_text)
    job_skills = extract_skills(job_text)

    # új AI alapú matching
    score = semantic_match(cv_text, job_text)

    print("=== AI JOB MATCH RESULT ===")
    print(f"CV skills: {cv_skills}")
    print(f"Job skills: {job_skills}")
    print(f"Semantic score: {score:.4f} (0-1 scale)")
    print(f"Semantic score: {score * 100:.2f}%")

if __name__ == "__main__":
    job_description = """
    We are looking for a Python developer with experience in:
    Python, FastAPI, Docker, AWS
    """

    run_pipeline("data/sample_cv.pdf", job_description)