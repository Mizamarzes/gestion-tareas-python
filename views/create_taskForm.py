import streamlit as st
from controllers.task_controller import create_task

def show_create_task_page():
    """
    Function to display the page for creating new tasks.
    """
    st.title("Create New Task")
    st.header("Add a New Task")
    title = st.text_input("Title")
    description = st.text_input("Description")

    if st.button("Add Task"):
        if title and description:
            try:
                create_task(title, description)  # Llamamos a la función para crear la tarea
                st.success("Task successfully created!")
            except Exception as e:
                st.error(f"Error creating task: {e}")
        else:
            st.error("Please fill in all fields.")
