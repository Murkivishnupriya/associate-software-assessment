from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)

    # Relationship with Comment model
    comments = relationship("Comment", back_populates="task", cascade="all, delete")


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String(500), nullable=False)
    task_id = Column(Integer, ForeignKey("tasks.id"))

    # Relationship back to Task model
    task = relationship("Task", back_populates="comments")

