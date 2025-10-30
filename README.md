# Associate Software Engineer (Python + React) – Assessment

**Developer:** Vishnupriya Murki  
**Email:** mvishnupriyaaa@gmail.com  

---

##  Overview

This repository contains my submission for the **Associate Software Engineer (Python + React)** assessment.  
It includes both backend and frontend implementations based on the open-source **Flask + React** template provided in the instructions.

The goal of this assessment is to demonstrate strong engineering practices, code structure, and understanding of full-stack development using **FastAPI (Python)** and **React.js**.

---

##  Tasks Completed

### **Task 1 – Backend APIs**
- Implemented CRUD APIs for managing **Tasks** and **Comments**.
- Followed RESTful conventions using **FastAPI** and **SQLAlchemy**.
- Added automated tests using **pytest** and **httpx**.
- Implemented SQLite as a lightweight relational database.
- Added **CORS** middleware to enable frontend communication.

**Endpoints include:**
| Method   | Endpoint               |       Description            |
|----------|------------------------|----------------------------=-|
| `POST`   | `/tasks/`              | Create a new task            |
| `GET`    | `/tasks/`              | Get all tasks                |
| `GET`    | `/tasks/{task_id}`     | Get a specific task          |
| `PUT`    | `/tasks/{task_id}`     | Update a task                |
| `DELETE` | `/tasks/{task_id}`     | Delete a task                |
| `POST`   | `/tasks/{task_id}/comments` | Add a comment to a task |

**Tests Executed:**

pytest -v

Task 2 – Frontend Interface

Built using React.js and Axios.

Implemented features to:

Add new tasks

View all tasks

Delete existing tasks

Integrated frontend with backend APIs.

Styled with clean, minimal UI following modern React standards.

Commands:

npm install
npm start


Frontend runs on http://localhost:3000

Backend runs on http://127.0.0.1:8000

##  Tech Stack

Backend:

FastAPI

SQLAlchemy

SQLite

Pydantic

Uvicorn

Pytest

Frontend:

React.js (Vite)

Axios

HTML / CSS / JS

##  Testing & Validation

Verified all CRUD operations using FastAPI’s Swagger UI (/docs).

Confirmed successful integration between frontend and backend.

Automated test suite (pytest) validates comment creation flow.

##  Video Walkthrough

A short demonstration video showcases:

Running backend and frontend locally.

Using the FastAPI Swagger UI to test APIs.

Executing automated tests.

Using the React UI to add, view, and delete tasks.

Overview of both Pull Requests.
https://www.awesomescreenshot.com/video/45850412?key=ab5bdc869502e71754abfbcbd3da0dc8

##  Pull Requests
Task	Description	PR Link
Task 1	FastAPI CRUD APIs for Tasks and Comments	Backend PR
 https://github.com/Murkivishnupriya/associate-software-assessment/pull/1

Task 2	React Task Manager Frontend	Frontend PR
 https://github.com/Murkivishnupriya/associate-software-assessment/pull/2

 Setup Instructions (Windows)
1️)  Clone Repository
git clone https://github.com/Murkivishnupriya/associate-software-assessment.git
cd associate-software-assessment

2️) Backend Setup
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload

3) Frontend Setup
cd frontend
npm install
npm start

##  Key Design Choices

Chose FastAPI for its simplicity, async support, and automatic documentation.

Added modular structure (models, schemas, crud, tests) for maintainability.

Used Axios in React for consistent API handling.

Emphasized clarity, code readability, and clean commit history.

##  Author

Vishnupriya Murki
 mvishnupriyaaa@gmail.com

 GitHub Profile

 Summary

This submission demonstrates:

Full-stack development with Python FastAPI and React.js

Proper software engineering practices

Automated testing

Clean, maintainable architecture

“Simplicity and reliability are at the core of great software.”
