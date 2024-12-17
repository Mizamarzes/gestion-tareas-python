import streamlit as st
import streamlit.components.v1 as components

def custom_alert(message: str):
    components.html(f"""
        <script type="text/javascript">
            alert("{message}");
        </script>
    """)

def sidebar_navigation():
    """
    Function to create the sidebar navigation for the task manager.
    """
    st.sidebar.title("Task Manager Navigation")
    # Aquí definimos las opciones de navegación
    # Cuando se hace clic en una opción, el contenido de la página se actualiza

