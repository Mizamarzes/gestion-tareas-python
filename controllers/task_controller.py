from models.task_model import TaskModel
from models.database import SessionLocal

# Create a task
def create_task(title, description):
    session = SessionLocal()
    new_task = TaskModel(title=title, description=description)
    session.add(new_task)
    session.commit()
    session.close()

# List all tasks
def list_tasks():
    session = SessionLocal()
    try:
        return session.query(TaskModel).all()  # No status filtering here
    finally:
        session.close()


# Update a task's status
def update_task_status(task_id, new_status):
    session = SessionLocal()
    task = session.query(TaskModel).filter_by(id=task_id).first()
    if task:
        task.status = new_status
        session.commit()
    session.close()

# Delete a task
def delete_task(task_id):
    session = SessionLocal()
    task = session.query(TaskModel).filter_by(id=task_id).first()
    if task:
        session.delete(task)
        session.commit()
    session.close()
