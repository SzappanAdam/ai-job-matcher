from src.extractor import extract_skills

def test_extract_skills():
    text = "Python SQL Docker."

    result = extract_skills(text)

    assert "python" in result
    assert "sql" in result
    assert "docker" in result

def test_case_insensitive():
    text = "PYTHON Docker"

    result = extract_skills(text)

    assert "python" in result
    assert "docker" in result

def test_unknown_skill():
    text = "Cobol"

    result = extract_skills(text)

    assert result == []

def test_duplicate_skill():
    text = "Python Python Python"

    result = extract_skills(text)

    assert result.count("python") == 1