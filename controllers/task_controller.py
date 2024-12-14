import pandas as pd
from io import BytesIO
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

# Update a task's title, description, and status
def update_task(task_id, new_title, new_description, new_status):
    session = SessionLocal()
    task = session.query(TaskModel).filter_by(id=task_id).first()
    if task:
        # Actualizar título, descripción y estado
        task.title = new_title
        task.description = new_description
        task.status = new_status
        session.commit()  # Guardar los cambios en la base de datos
        session.close()
        return task  # Retornar la tarea actualizada
    session.close()
    return None  # Si no se encuentra la tarea, retornar None

# Función para exportar las tareas a un archivo Excel
def export_tasks_to_excel():
    session = SessionLocal()
    tasks = session.query(TaskModel).all()  # Obtener todas las tareas

    # Crear una lista de diccionarios con los datos de las tareas
    tasks_data = []
    for task in tasks:
        task_data = {
            'ID': task.id,
            'Title': task.title,
            'Description': task.description,
            'Status': task.status.value
        }
        tasks_data.append(task_data)

    # Crear un DataFrame de pandas
    df = pd.DataFrame(tasks_data)

    # Crear un archivo Excel en memoria
    output = BytesIO()

    # Guardar el DataFrame en el archivo Excel
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Tasks')

    # Mover el puntero al principio del archivo para leerlo
    output.seek(0)
    return output

# Delete a task
def delete_task(task_id):
    session = SessionLocal()
    task = session.query(TaskModel).filter_by(id=task_id).first()
    if task:
        session.delete(task)
        session.commit()
    session.close()



    