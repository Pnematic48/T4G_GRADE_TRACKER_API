from pydantic import BaseModel
from typing import Optional, List



# ── Student schemas ──────────────────────

class StudentCreate(BaseModel):
    name: str
    email: str


class GradeOut(BaseModel):
    id: int
    subject: str
    score: float

    class Config:
        from_attributes = True


class StudentOut(BaseModel):
    id: int
    name: str
    email: str
    grades: List[GradeOut] = []

    class Config:
        from_attributes = True


# ── Grade schemas ──────────────────────

class GradeCreate(BaseModel):
    subject: str
    score: float


class GradeAdded(BaseModel):
    id: int
    student_id: int
    subject: str
    score: float

    class Config:
        from_attributes = True
