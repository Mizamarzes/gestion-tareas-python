from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Configuración de la base de datos
DATABASE_URL = "sqlite:///task_manager.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Base para los modelos
Base = declarative_base()

# Configuración de la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """
    Inicializa la base de datos creando las tablas solo si no existen.
    """
    # Verificar si el archivo de la base de datos ya existe
    if not os.path.exists("task_manager_db.db"):
        try:
            from models.task_model import TaskModel  # Importa los modelos aquí para registrarlos
            Base.metadata.create_all(bind=engine)  # Crea las tablas solo si no existen
            print("Base de datos inicializada correctamente.")
        except Exception as e:
            print(f"Error al inicializar la base de datos: {e}")
    else:
        print("La base de datos ya existe. No es necesario crear las tablas nuevamente.")
