from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración del motor de base de datos
DATABASE_URL = "sqlite:///gestor_tareas.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Base para los modelos
Base = declarative_base()

# Configuración de la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """
    Inicializa la base de datos creando todas las tablas definidas en los modelos.
    """
    try:
        from models.tarea_model import TareaModel  # Importa los modelos aquí para registrarlos
        Base.metadata.create_all(bind=engine)
        print("Base de datos inicializada correctamente.")
    except Exception as e:
        print(f"Error al inicializar la base de datos: {e}")

