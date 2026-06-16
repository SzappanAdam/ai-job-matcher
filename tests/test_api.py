from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)

def test_root():
    response = client.get("/")

    assert response.status_code == 200

def test_match_endpoint():
    response = client.post(
        "/match",
        json={
            "cv_text": "Python Docker",
            "job_text": "Python AWS"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "score" in data
    assert "missing_skills" in data