import streamlit as st
from controllers.controller import crear_tarea, listar_tareas, actualizar_estado_tarea, eliminar_tarea
from models.model import EstadoTarea, init_db

# Inicializar la base de datos
init_db()

st.title("Gestor de Tareas")

# Crear nueva tarea
st.header("Crear Nueva Tarea")
titulo = st.text_input("Título")
descripcion = st.text_input("Descripción")
if st.button("Agregar Tarea"):
    if titulo and descripcion:
        crear_tarea(titulo, descripcion)
        st.success("¡Tarea creada con éxito!")
    else:
        st.error("Por favor completa todos los campos.")

# Listar tareas
st.header("Lista de Tareas")
tareas = listar_tareas()
for tarea in tareas:
    st.write(f"**ID:** {tarea.id} | **Título:** {tarea.titulo} | **Estado:** {tarea.estado.value}")
    if st.button(f"Completar Tarea {tarea.id}"):
        actualizar_estado_tarea(tarea.id, EstadoTarea.COMPLETADA)
        st.experimental_rerun()
    if st.button(f"Eliminar Tarea {tarea.id}"):
        eliminar_tarea(tarea.id)
        st.experimental_rerun()

