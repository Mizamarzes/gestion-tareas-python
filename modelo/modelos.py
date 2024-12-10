from sqlalchemy import Column
from sqlalchemy import String, Integer, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class TareaModel(Base):
    __tablename__="tarea"
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(150))
    descripcion = Column(String(150))
    estado = Column()