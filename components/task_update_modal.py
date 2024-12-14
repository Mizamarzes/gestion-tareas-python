import streamlit as st
from components.alert import show_alert
from controllers.task_controller import update_task_in_db

# Componente modal para actualizar tarea
def task_update_modal(task):
    with st.expander(f"Update Task {task.id}", expanded=True):  # Expander para simular un modal
        with st.form(key=f"update_form_{task.id}"):  # Formulario para actualizar tarea
            new_title = st.text_input("New Title", value=task.title)
            new_description = st.text_area("New Description", value=task.description)
            
            submit_button = st.form_submit_button(label="Update Task")
            
            if submit_button:
                # Llamar a la función del controlador para actualizar la tarea
                updated_task = update_task_in_db(task.id, new_title, new_description)
                if updated_task:
                    show_alert("success", f"Task {task.id} updated successfully!")
                else:
                    show_alert("error", f"Failed to update task {task.id}. Please try again.")
