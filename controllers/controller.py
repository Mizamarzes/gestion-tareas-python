from models.model import TareaModel, EstadoTarea, SessionLocal

# Crear una tarea
def crear_tarea(titulo, descripcion):
    session = SessionLocal()
    nueva_tarea = TareaModel(titulo=titulo, descripcion=descripcion)
    session.add(nueva_tarea)
    session.commit()
    session.close()

# Listar todas las tareas
def listar_tareas():
    session = SessionLocal()
    tareas = session.query(TareaModel).all()
    session.close()
    return tareas

# Actualizar una tarea
def actualizar_estado_tarea(tarea_id, nuevo_estado):
    session = SessionLocal()
    tarea = session.query(TareaModel).filter_by(id=tarea_id).first()
    if tarea:
        tarea.estado = nuevo_estado
        session.commit()
    session.close()

# Eliminar una tarea
def eliminar_tarea(tarea_id):
    session = SessionLocal()
    tarea = session.query(TareaModel).filter_by(id=tarea_id).first()
    if tarea:
        session.delete(tarea)
        session.commit()
    session.close()
