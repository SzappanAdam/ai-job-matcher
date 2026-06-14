from src.extractor import extract_skills

def test_extract_skills():
    text = "I work with Python, SQL and Docker."
    result = extract_skills(text)

    assert "python" in result
    assert "sql" in result
    assert "docker" in result