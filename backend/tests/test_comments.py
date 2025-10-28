import sys
import os

# Add backend root to import path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_task_and_comment():
    # Create a new task
    task_response = client.post("/tasks/", json={
        "title": "Test Task",
        "description": "Task for automated testing"
    })
    assert task_response.status_code == 200
    task_data = task_response.json()
    task_id = task_data["id"]

    # Create a comment on that task
    comment_response = client.post(f"/tasks/{task_id}/comments", json={"text": "Initial comment"})
    assert comment_response.status_code == 200
    comment_data = comment_response.json()
    assert comment_data["text"] == "Initial comment"
    assert comment_data["task_id"] == task_id
    comment_id = comment_data["id"]

    # Fetch all comments for the task
    all_comments = client.get(f"/tasks/{task_id}/comments")
    assert all_comments.status_code == 200
    comments_list = all_comments.json()
    assert len(comments_list) > 0
    assert comments_list[0]["text"] == "Initial comment"

    # Update the comment
    updated = client.put(f"/comments/{comment_id}", json={"text": "Updated text"})
    assert updated.status_code == 200
    assert updated.json()["text"] == "Updated text"

    # Delete the comment
    deleted = client.delete(f"/comments/{comment_id}")
    assert deleted.status_code == 200
    assert deleted.json()["message"] == "Comment deleted successfully"

    # Cleanup: delete the task
    client.delete(f"/tasks/{task_id}")
