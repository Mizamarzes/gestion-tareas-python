from sqlalchemy import Column, String, Integer, Enum
import enum
from models.database import Base

# Define the enumerator for the task status
class TaskStatus(enum.Enum):
    PENDING = "pending"
    COMPLETED = "completed"

# Define the model for the Task table
class TaskModel(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(150), nullable=False)
    description = Column(String(150), nullable=False)
    status = Column(Enum(TaskStatus), default=TaskStatus.PENDING, nullable=False)
