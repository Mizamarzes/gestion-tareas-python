from sqlalchemy import Column, String, Integer, Enum
import enum
from models.database import Base


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

