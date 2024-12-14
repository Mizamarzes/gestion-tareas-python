import streamlit as st
import streamlit.components.v1 as components

def custom_alert(message: str):
    components.html(f"""
        <script type="text/javascript">
            alert("{message}");
        </script>
    """)
