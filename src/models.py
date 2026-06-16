from pydantic import BaseModel
from typing import List

class MatchResponse(BaseModel):
    score: float
    matching_skills: List[str]
    missing_skills: List[str]
    