from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Student, Grade
from app.schemas import (
    StudentCreate, StudentOut,
    GradeCreate, GradeAdded
)

router = APIRouter()


#Add a new student 
@router.post("/students", 
    response_model=StudentOut,
    status_code=status.HTTP_201_CREATED)
def add_student(data: StudentCreate, db: Session = Depends(get_db)):
    existing = db.query(Student).filter(
        Student.email == data.email
    ).first()
    if existing:
        raise HTTPException(
            status_code=400,
            detail="A student with this email already exists."
        )
    student = Student(name=data.name, email=data.email)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student


#Get all students
@router.get("/students",
    response_model=list[StudentOut])
def get_all_students(db: Session = Depends(get_db)):
    students = db.query(Student).all()
    if not students:
        raise HTTPException(
            status_code=404,
            detail="No students found."
        )
    return students


#Get one student
@router.get("/students/{student_id}",
    response_model=StudentOut)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(
        Student.id == student_id
    ).first()
    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found."
        )
    return student


#Add a grade
@router.post("/students/{student_id}/grades",
    response_model=GradeAdded,
    status_code=status.HTTP_201_CREATED)
def add_grade(student_id: int, data: GradeCreate, 
    db: Session = Depends(get_db)):
    student = db.query(Student).filter(
        Student.id == student_id
    ).first()
    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found."
        )
    grade = Grade(
        subject=data.subject,
        score=data.score,
        student_id=student_id
    )
    db.add(grade)
    db.commit()
    db.refresh(grade)
    return grade


# Get all grades for a student
@router.get("/students/{student_id}/grades",
    response_model=list[GradeAdded])
def get_grades(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(
        Student.id == student_id
    ).first()
    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found."
        )
    return student.grades


#Get student average
@router.get("/students/{student_id}/average")
def get_average(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(
        Student.id == student_id
    ).first()
    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found."
        )
    if not student.grades:
        return {"message": "No grades recorded yet."}
    
    total = sum(g.score for g in student.grades)
    average = round(total / len(student.grades), 2)
    return {
        "student": student.name,
        "average_score": average,
        "total_subjects": len(student.grades)
    }