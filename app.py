import streamlit as st
from controllers.task_controller import create_task, list_tasks, update_task_status, delete_task
from models.task_model import TaskStatus
from models.database import init_db

#components
from components.alert import custom_alert

# Initialize the database
init_db()

st.title("Task Manager")

# Create a new task
st.header("Create New Task")
title = st.text_input("Title")
description = st.text_input("Description")
if st.button("Add Task"):
    if title and description:
        create_task(title, description)
        st.success("Task successfully created!")
    else:
        st.error("Please fill in all fields.")

# Display tasks in a table
st.header("Task List")

# Get all tasks without filtering
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
        # Create a row for each task
        col1, col2, col3, col4, col5, col6, col7 = st.columns([1, 3, 3, 2, 1, 1, 1])
        col1.write(task.id)
        col2.write(task.title)
        col3.write(task.description)
        
        # Display state with color
        if task.status == TaskStatus.PENDING:
            col4.markdown("🔴**Pending**")
        elif task.status == TaskStatus.COMPLETED:
            col4.markdown("🟢**Completed**")
        
        # Complete button
        with col5:
            if task.status == TaskStatus.PENDING:
                if st.button("✔️", key=f"complete_{task.id}"):
                    update_task_status(task.id, TaskStatus.COMPLETED)
                    st.rerun()

        # Delete button
        with col6:
            if st.button("❌", key=f"delete_{task.id}"):
                delete_task(task.id)
                st.rerun()

        # Update button
        with col7:
            if st.button("⚙", key=f"update_{task.id}"):
                # Add your logic to update a task
                custom_alert(f"Update functionality for tasks not implemented yet.")
