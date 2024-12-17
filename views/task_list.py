import streamlit as st
from controllers.task_controller import list_tasks, update_task, delete_task
from models.task_model import TaskStatus
from components.components import custom_alert

def show_task_list_page():
    st.title("Task List")
    st.header("Your Tasks")

    tasks = list_tasks()

    if not tasks:
        st.write("No tasks to display.")
    else:
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

            if task.status == TaskStatus.PENDING:
                col4.markdown("🔴**Pending**")
            elif task.status == TaskStatus.COMPLETED:
                col4.markdown("🟢**Completed**")

            with col5:
                if task.status == TaskStatus.PENDING:
                    if st.button("✔️", key=f"complete_{task.id}"):
                        update_task(task.id, task.title, task.description, TaskStatus.COMPLETED)
                        st.rerun()

            with col6:
                if st.button("❌", key=f"delete_{task.id}"):
                    delete_task(task.id)
                    st.rerun()

            with col7:
                if st.button("⚙", key=f"update_{task.id}"):
                    custom_alert("Update functionality coming soon!")
