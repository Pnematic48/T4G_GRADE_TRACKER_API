from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    grades= relationship("Grade",back_populates="student")

class Grade(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String(100), nullable=False)
    score = Column(Float, nullable=False)
    student_id =Column(Integer, ForeignKey("students.id"),nullable=False)

    student= relationship("Student",back_populates="grades")
    

