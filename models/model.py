from sqlalchemy import Column, String, Integer, Enum, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import enum

Base = declarative_base()

# Definir el enumerador para el estado de la tarea
class EstadoTarea(enum.Enum):
    PENDIENTE = "pendiente"
    COMPLETADA = "completada"

# Definir el modelo de la tabla Tarea
class TareaModel(Base):
    __tablename__ = "tarea"
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(150), nullable=False)
    descripcion = Column(String(150), nullable=False)
    estado = Column(Enum(EstadoTarea), default=EstadoTarea.PENDIENTE, nullable=False)

# Configurar la base de datos
DATABASE_URL = "sqlite:///gestor_tareas.db"  # Puedes cambiar a otra base de datos
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

# Crear las tablas
def init_db():
    Base.metadata.create_all(engine)