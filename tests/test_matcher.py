from src.matcher import calculate_match
from src.matcher import analyze_skills

def test_perfect_match():
    assert calculate_match(
        ["python", "docker"],
        ["python", "docker"]
    ) == 100

def test_partial_match():
    score = calculate_match(
        ["python", "docker"],
        ["python", "aws"]
    )

    assert score > 0
    assert score < 100

def test_no_match():
    score = calculate_match(
        ["python"],
        ["aws"]
    )

    assert score == 0

def test_missing_skill_detection():
    result = analyze_skills(
        ["python", "docker"],
        ["python", "docker", "aws"]
    )

    assert result["missing_skills"] == ["aws"]

def test_matching_skill_detection():
    result = analyze_skills(
        ["python", "docker"],
        ["python", "docker", "aws"]
    )

    assert result["matching_skills"] == [
        "docker",
        "python"
    ]