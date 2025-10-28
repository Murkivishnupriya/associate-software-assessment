from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import models, schemas
from database import SessionLocal, engine

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Enable CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root route (optional)
@app.get("/")
def read_root():
    return {"message": "FastAPI backend running successfully!"}

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ----------------------------------------------------------
# TASK CRUD
# ----------------------------------------------------------

@app.post("/tasks/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    db_task = models.Task(title=task.title, description=task.description)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


@app.get("/tasks/", response_model=list[schemas.Task])
def get_tasks(db: Session = Depends(get_db)):
    return db.query(models.Task).all()


@app.get("/tasks/{task_id}", response_model=schemas.Task)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.put("/tasks/{task_id}", response_model=schemas.Task)
def update_task(task_id: int, updated_task: schemas.TaskCreate, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task.title = updated_task.title
    task.description = updated_task.description
    db.commit()
    db.refresh(task)
    return task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"message": "Task deleted successfully"}


# ----------------------------------------------------------
# COMMENTS CRUD (for each task)
# ----------------------------------------------------------

@app.post("/tasks/{task_id}/comments", response_model=schemas.Comment)
def create_comment(task_id: int, comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db_comment = models.Comment(text=comment.text, task_id=task_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


@app.get("/tasks/{task_id}/comments", response_model=list[schemas.Comment])
def get_comments(task_id: int, db: Session = Depends(get_db)):
    comments = db.query(models.Comment).filter(models.Comment.task_id == task_id).all()
    return comments


@app.put("/comments/{comment_id}", response_model=schemas.Comment)
def update_comment(comment_id: int, updated_comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    comment = db.query(models.Comment).filter(models.Comment.id == comment_id).first()
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    comment.text = updated_comment.text
    db.commit()
    db.refresh(comment)
    return comment


@app.delete("/comments/{comment_id}")
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    comment = db.query(models.Comment).filter(models.Comment.id == comment_id).first()
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    db.delete(comment)
    db.commit()
    return {"message": "Comment deleted successfully"}
