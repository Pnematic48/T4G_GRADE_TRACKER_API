# T4G Grade Tracker API
> A backend system for managing student grades across subjects.

## The Problem
Many schools still track student grades manually in 
spreadsheets. This API gives any application a proper 
way to store and retrieve student results.

## What It Does
1. Register and manage students
2. Record grades per subject for each student
3. Retrieve a student's full grade history
4. Calculate a student's average score automatically

## Tech Stack
1. Python
2. FastAPI
3. SQLAlchemy
4. MySQL
5. Uvicorn
6. python-dotenv

## How to Run It Locally

1. Clone the repository
git clone https://github.com/Pnematic48/T4G_GRADE_TRACKER_API.git
cd T4G_GRADE_TRACKER_API

2. Create and activate virtual environment
python3 -m venv datavenv
source datavenv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Set up your .env file
DATABASE_URL=mysql+mysqlconnector://root:yourpassword@localhost:3306/t4g_grades

5. Run the server
uvicorn main:app --reload

6. Visit the docs
http://127.0.0.1:8000/docs

## API Endpoints
| Method | Path | What It Does |
|--------|------|-------------|
| POST | /api/students | Register a student |
| GET | /api/students | List all students |
| GET | /api/students/{id} | Get one student |
| DELETE | /api/students/{id} | Remove a student |
| POST | /api/students/{id}/grades | Add a grade |
| GET | /api/students/{id}/grades | Get all grades |
| GET | /api/students/{id}/average | Get average score |

## Example Request
POST /api/students
{
  "name": "Monica Sarpong",
  "email": "mosarps.48@gmail.com"
}

## Example Response
{
  "id": 1,
  "name": "Monica Sarpong",
  "email": "mosarps.48@gmail.com",
  "grades": 89.7
}