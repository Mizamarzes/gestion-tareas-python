# Gestor de Tareas 

### Juan Diego Contreras Melendez 

Este es un sistema de gestión de tareas desarrollado con Python, Streamlit y SQLAlchemy. Permite a los usuarios crear, visualizar, actualizar y eliminar tareas, así como exportar la lista de tareas a un archivo Excel.

## Requisitos

Para ejecutar esta aplicación, necesitarás tener instalado lo siguiente:

- Python: Asegurate de tener Python 3.7 o superior.
- Dependencias de Python: Asegúrate de tener las siguientes librerías instaladas

```bash
pip install -r requirements.txt
```

Dependencias necesarias:

```
SQLAlchemy==1.4.49
streamlit
pandas
openpyxl
```

## Ejecutar la aplicación

Para ejecutar la aplicación, simplemente ejecuta el siguiente comando en tu terminal:

```bash
streamlit run app.py
```

Este comando abrirá una nueva ventana del navegador con la interfaz de la aplicación.

## Uso de la Aplicación

Una vez que la aplicación esté en funcionamiento, podrás interactuar con ella a través de la interfaz proporcionada por Streamlit. Las principales funcionalidades disponibles son:

### 1. **Crear una nueva tarea**

- En la sección **"Create New Task"**, ingresa el título y la descripción de la tarea.
- Haz clic en el botón **"Add Task"** para agregar la tarea.
- Si todos los campos están llenos, la tarea se creará y aparecerá en la lista de tareas.

### 2. **Ver la lista de tareas**

- En la sección **"Task List"**, verás todas las tareas que has creado.
- Cada tarea mostrará:
  - **ID**: Identificador único de la tarea.
  - **Title**: Título de la tarea.
  - **Description**: Descripción de la tarea.
  - **Status**: Estado de la tarea (Pendiente o Completada).
  - Botones de acción:
    - **✔️**: Marca la tarea como completada (si está pendiente).
    - **❌**: Elimina la tarea.
    - **⚙**: Permite actualizar los detalles de la tarea.

### 3. **Exportar tareas a Excel**

- En la sección **"Export Tasks to Excel"**, puedes hacer clic en el botón **"Export to Excel"**.
- Esto generará un archivo Excel con la lista de tareas.
- Una vez generado, podrás descargar el archivo haciendo clic en el botón **"Download Excel File"**.

## Estructura del Proyecto

La estructura del proyecto es la siguiente:

```bash
│
├── app.py                  # Aplicación Streamlit
├── controllers/            # Lógica de negocio (crear, listar, actualizar, eliminar tareas)
│   └── task_controller.py  # Controlador de tareas
├── models/                 # Definición de la base de datos y modelo de tareas
│   ├── task_model.py       # Modelo de tareas (SQLAlchemy)
│   └── database.py         # Conexión a la base de datos
├── components/             # Componentes reutilizables
│   └── components.py       # Componentes personalizados para la app
├── requirements.txt        # Dependencias del proyecto
└── README.md               # Documentación del proyecto
```