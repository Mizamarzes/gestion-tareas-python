import streamlit as st
from controllers.task_controller import (
    create_task, list_tasks, update_task, delete_task,
    export_tasks_to_excel, export_tasks_to_json, import_tasks_from_json
)
from models.task_model import TaskStatus
from models.database import init_db
from components.components import custom_alert
import json

# --------------------- Database Initialization ---------------------
def initialize_database():
    """
    Function to initialize the database only once using st.session_state.
    """
    if "db_initialized" not in st.session_state:
        init_db()
        st.session_state.db_initialized = True

initialize_database()  # Ensures DB is initialized only once

# ----------------------- Sidebar Navigation -----------------------
st.sidebar.title("Task Manager Navigation")
page = st.sidebar.radio("Go to:", ["Create Task", "Task List", "Import/Export Tasks"])

# ------------------- Page 1: Create Task --------------------------
if page == "Create Task":
    st.title("Create New Task")
    st.header("Add a New Task")

    title = st.text_input("Title")
    description = st.text_input("Description")

    if st.button("Add Task"):
        if title and description:
            try:
                create_task(title, description)  # Llamamos a la función que crea la tarea
                st.success("Task successfully created!")  # Mensaje de éxito
            except Exception as e:
                st.error(f"Error creating task: {e}")  # Muestra un error si la creación falla
        else:
            st.error("Please fill in all fields.")

# ------------------ Page 2: Task List -----------------------------
elif page == "Task List":
    st.title("Task List")
    st.header("Your Tasks")

    tasks = list_tasks()

    if not tasks:
        st.write("No tasks to display.")
    else:
        # Table header
        col1, col2, col3, col4, col5, col6, col7 = st.columns([1, 3, 3, 2, 1, 1, 1])
        col1.write("**ID**")
        col2.write("**Title**")
        col3.write("**Description**")
        col4.write("**Status**")
        col5.write("")
        col6.write("")
        col7.write("")

        for task in tasks:
            col1, col2, col3, col4, col5, col6, col7 = st.columns([1, 3, 3, 2, 1, 1, 1])
            col1.write(task.id)
            col2.write(task.title)
            col3.write(task.description)

            # Status display
            if task.status == TaskStatus.PENDING:
                col4.markdown("🔴**Pending**")
            elif task.status == TaskStatus.COMPLETED:
                col4.markdown("🟢**Completed**")

            # Complete button
            with col5:
                if task.status == TaskStatus.PENDING:
                    if st.button("✔️", key=f"complete_{task.id}"):
                        update_task(task.id, task.title, task.description, TaskStatus.COMPLETED)
                        st.rerun()

            # Delete button
            with col6:
                if st.button("❌", key=f"delete_{task.id}"):
                    delete_task(task.id)
                    st.rerun()

            # Update button
            with col7:
                if st.button("⚙", key=f"update_{task.id}"):
                    custom_alert("Update functionality coming soon!")

# ---------------- Page 3: Import & Export Tasks -------------------
elif page == "Import/Export Tasks":
    st.title("Import & Export Tasks")
    st.header("Manage Your Tasks")

    # Export to Excel
    if st.button("Export Tasks to Excel"):
        excel_file = export_tasks_to_excel()
        if excel_file:
            st.download_button(
                label="Download Excel",
                data=excel_file,
                file_name="tasks.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        else:
            st.error("Failed to export tasks to Excel.")

    # Export to JSON
    if st.button("Export Tasks to JSON"):
        json_file = export_tasks_to_json()
        if json_file:
            st.download_button(
                label="Download JSON",
                data=json_file,
                file_name="tasks.json",
                mime="application/json"
            )
        else:
            st.error("Failed to export tasks to JSON.")

    # Import from JSON
    st.subheader("Import Tasks from JSON")
    uploaded_file = st.file_uploader("Choose a JSON file", type=["json"])

    if uploaded_file is not None:
        try:
            import_tasks_from_json(uploaded_file)  # Intentamos importar las tareas
            st.success("Tasks imported successfully!")
            st.rerun()
        except Exception as e:
            st.error(f"Error: {e}")  # Si ocurre un error, lo mostramos al usuario
