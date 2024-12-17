import streamlit as st
from controllers.task_controller import export_tasks_to_excel, export_tasks_to_json, import_tasks_from_json

def show_import_export_tasks_page():
    st.title("Import & Export Tasks")
    st.header("Manage Your Tasks")

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

    st.subheader("Import Tasks from JSON")
    uploaded_file = st.file_uploader("Choose a JSON file", type=["json"])

    if uploaded_file is not None:
        try:
            import_tasks_from_json(uploaded_file)
            st.success("Tasks imported successfully!")
            st.rerun()
        except Exception as e:
            st.error(f"Error: {e}")
