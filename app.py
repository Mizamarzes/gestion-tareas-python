import streamlit as st
from components import sidebar_navigation
from views.create_taskForm import show_create_task_page
from views.task_list import show_task_list_page
from views.import_export import show_import_export_tasks_page
from models.database import init_db  # Asumiendo que tienes la función init_db en un archivo database.py

# ---------------------- Inicializar la base de datos ----------------------
# Llamamos a la función de inicialización solo una vez cuando la aplicación se inicie
init_db()

# ---------------------- Sidebar Navigation ----------------------
sidebar_navigation()

# ---------------------- Page Navigation -------------------------
page = st.sidebar.radio("Go to:", ["Create Task", "Task List", "Import/Export Tasks"])

# --------------------- Display Content Based on Selection -------------------------
if page == "Create Task":
    show_create_task_page()

elif page == "Task List":
    show_task_list_page()

elif page == "Import/Export Tasks":
    show_import_export_tasks_page()
