import streamlit as st
from controllers.tarea_controller import crear_tarea, listar_tareas, actualizar_estado_tarea, eliminar_tarea
from models.tarea_model import EstadoTarea
from models.database import init_db

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

# Filtros de tareas
st.header("Filtrar Tareas")
columna_1, columna_2 = st.columns(2)
with columna_1:
    tareas_pendientes = st.button("Ver Tareas Pendientes")
with columna_2:
    tareas_completadas = st.button("Ver Tareas Completadas")

# Obtener tareas según el filtro
if tareas_pendientes:
    tareas = listar_tareas(EstadoTarea.PENDIENTE)
elif tareas_completadas:
    tareas = listar_tareas(EstadoTarea.COMPLETADA)
else:
    tareas = listar_tareas()

# Mostrar tareas
st.header("Lista de Tareas")
for tarea in tareas:
    # Crear un layout de columnas para cada tarea
    col1, col2, col3, col4 = st.columns([3, 4, 3, 3])
    
    with col1:
        st.write(f"**ID:** {tarea.id} | **Título:** {tarea.titulo}")
    
    with col2:
        st.write(f"**Descripción:** {tarea.descripcion}")
    
    with col3:
        if tarea.estado == EstadoTarea.PENDIENTE:
            st.markdown(f"**Estado:** :red[Pendiente]")
        elif tarea.estado == EstadoTarea.COMPLETADA:
            st.markdown(f"**Estado:** :green[Completada]")

    with col4:
        if tarea.estado == EstadoTarea.PENDIENTE:
            if st.button(f"Completar Tarea"):
                actualizar_estado_tarea(tarea.id, EstadoTarea.COMPLETADA)
                st.rerun()
        
        if st.button(f"Eliminar Tarea "):
            eliminar_tarea(tarea.id)
            st.rerun()
