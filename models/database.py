from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database engine configuration
DATABASE_URL = "sqlite:///task_manager_db.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Base class for models
Base = declarative_base()

# Session configuration
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """
    Initializes the database by creating all tables defined in the models.
    """
    try:
        from models.task_model import TaskModel  # Import the models here to register them
        Base.metadata.create_all(bind=engine)
        print("Database initialized correctly.")
    except Exception as e:
        print(f"Error initializing the database: {e}")
