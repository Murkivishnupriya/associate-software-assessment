# Associate Software Engineer (Python + React) Assessment

##  Overview
This project is a full-stack implementation for the **Associate Software Engineer Assessment**.  
It includes a backend API built with **FastAPI** and a frontend web interface built with **ReactJS**.

The application allows users to:
- Manage **Tasks** (Add, View, Delete)
- Manage **Comments** for each task (Add, Edit, Delete)
- Run automated tests to validate API functionality

---

##  Tech Stack
 ______________________________________________________________
| Layer        |              Technology                       |
|--------------|-----------------------------------------------|
| **Backend**  | FastAPI (Python 3.11), SQLAlchemy ORM, SQLite |
| **Frontend** | ReactJS, Axios, JavaScript (ES6), HTML5, CSS3 |
| **Testing**  | Pytest, FastAPI TestClient                    |
| **Database** | SQLite (auto-created)                         |

---

## Folder Structure

associate-software-assessment/
│
├── backend/
│ ├── main.py # FastAPI app
│ ├── models.py # Database models (Task, Comment)
│ ├── schemas.py # Pydantic models for validation
│ ├── database.py # SQLite connection and Base setup
│ ├── tests/
│ │ └── test_comments.py # Automated test cases (pytest)
│ └── tasks.db # SQLite database file (auto-created)
│
└── frontend/
├── src/ # React source code
├── package.json
├── public/
└── (other React files)



---

##  Backend Setup (FastAPI)

### Create and activate a virtual environment

cd backend
python -m venv venv
venv\Scripts\activate   # (Windows)


## Install dependencies

pip install fastapi uvicorn sqlalchemy pydantic httpx pytest


## Run the server

uvicorn main:app --reload

## Databases
Uses SQLite (tasks.db)

Automatically created at runtime.

ORM handled by SQLAlchemy.



## Run Tests (Pytest)
pytest -v


## Output:
tests/test_comments.py::test_create_task_and_comment PASSED


##### Frontend Setup (React)
Go to frontend directory

cd ../frontend


## Install dependencies
npm install


## Run the React app
npm start

## Features
1) Task Management

Create a task (title, description)

View list of tasks

Delete tasks

2) Comment Management

Add comment to a specific task

Edit or delete comment

3) Testing

Full test coverage for Task + Comment CRUD APIs using pytest




## AUTHOR 
VISHNUPRIYA MURKI 
mvishnupriyaaa@gmail.com