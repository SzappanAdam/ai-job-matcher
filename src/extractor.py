import re  # regex

KNOWN_SKILLS = {
    "python", "sql", "docker", "aws", "ml", "machine learning",
    "pandas", "numpy", "fastapi"
}

def extract_skills(text: str):
    text = text.lower()

    found = set()  # set() - Duplikációk eltűnnek

    for skill in KNOWN_SKILLS:
        if re.search(rf"\b{re.escape(skill)}\b", text):   # \bskill\b - Csak teljes szót talál meg
            found.add(skill)

    return list(found)