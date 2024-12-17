import pandas as pd
import json
from io import BytesIO
from sqlalchemy.exc import SQLAlchemyError
from models.task_model import TaskModel, TaskStatus
from models.database import SessionLocal

# Create a task
def create_task(title, description):
    session = SessionLocal()
    try:
        new_task = TaskModel(title=title, description=description)
        session.add(new_task)
        session.commit()
        print("Task created successfully")  # Puedes ver este mensaje en la consola para depurar
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error creating task: {e}")
        raise Exception(f"Error creating task: {e}")  # Lanza una excepción que capturamos en el frontend
    finally:
        session.close()


# List all tasks
def list_tasks():
    session = SessionLocal()
    try:
        return session.query(TaskModel).all()
    except SQLAlchemyError as e:
        print(f"Error al listar tareas: {e}")
        return []  # Retorna una lista vacía si hay un error
    finally:
        session.close()


# Update a task's title, description, and status
def update_task(task_id, new_title, new_description, new_status):
    session = SessionLocal()
    try:
        task = session.query(TaskModel).filter_by(id=task_id).first()
        if task:
            task.title = new_title
            task.description = new_description
            task.status = new_status
            session.commit()
            return task  # Retorna la tarea actualizada
        else:
            print("Tarea no encontrada.")
            return None
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error al actualizar la tarea: {e}")
        return None
    finally:
        session.close()


# Export tasks to Excel
def export_tasks_to_excel():
    session = SessionLocal()
    try:
        tasks = session.query(TaskModel).all()
        tasks_data = [
            {
                'ID': task.id,
                'Title': task.title,
                'Description': task.description,
                'Status': task.status.value
            }
            for task in tasks
        ]

        # Crear un DataFrame
        df = pd.DataFrame(tasks_data)

        # Exportar a Excel en memoria
        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Tasks')

        output.seek(0)
        return output
    except SQLAlchemyError as e:
        print(f"Error al obtener tareas para exportación: {e}")
        return None
    except Exception as e:
        print(f"Error al exportar tareas a Excel: {e}")
        return None
    finally:
        session.close()

# Export tasks to a JSON file
def export_tasks_to_json():
    session = SessionLocal()
    try:
        tasks = session.query(TaskModel).all()
        tasks_data = [
            {
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "status": task.status.value
            }
            for task in tasks
        ]
        # Guardar el JSON en memoria
        output = BytesIO()
        output.write(json.dumps(tasks_data, indent=4).encode('utf-8'))
        output.seek(0)
        return output
    except SQLAlchemyError as e:
        print(f"Error al exportar tareas a JSON: {e}")
        return None
    finally:
        session.close()


# Import tasks from a JSON file
def import_tasks_from_json(json_file):
    """
    Import tasks from a JSON file and avoid duplicates.
    """
    session = SessionLocal()
    try:
        # Cargar datos del archivo JSON
        tasks_data = json.load(json_file)  # Puede lanzar un error si el JSON es inválido

        for task_data in tasks_data:
            # Validar si la tarea ya existe en la base de datos
            existing_task = session.query(TaskModel).filter_by(
                title=task_data["title"],
                description=task_data["description"]
            ).first()

            if not existing_task:
                # Crear nueva tarea si no existe
                new_task = TaskModel(
                    title=task_data["title"],
                    description=task_data["description"],
                    status=TaskStatus(task_data["status"])  # Convertir estado
                )
                session.add(new_task)
        session.commit()  # Confirmar los cambios
    except json.JSONDecodeError as e:
        print(f"Invalid JSON format: {e}")  # Captura el error si el JSON no es válido
        raise Exception(f"Invalid JSON format: {e}")  # Lanza un mensaje claro para el frontend
    except Exception as e:
        print(f"Error importing tasks: {e}")
        session.rollback()
        raise Exception(f"Error importing tasks: {e}")
    finally:
        session.close()

# Delete a task
def delete_task(task_id):
    session = SessionLocal()
    try:
        task = session.query(TaskModel).filter_by(id=task_id).first()
        if task:
            session.delete(task)
            session.commit()
            print(f"Tarea {task_id} eliminada correctamente.")
        else:
            print("Tarea no encontrada.")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error al eliminar la tarea: {e}")
    finally:
        session.close()
