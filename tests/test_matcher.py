from src.matcher import calculate_match

def test_basic_match():
    cv = ["python", "sql", "docker"]
    job = ["python", "docker", "aws"]

    assert calculate_match(cv, job) == 50.0
