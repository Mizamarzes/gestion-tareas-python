# Gestor de Tareas

### Juan Diego Contreras Melendez

Este es un sistema de gestión de tareas desarrollado con Python, Streamlit y SQLAlchemy. Permite a los usuarios crear, visualizar, actualizar y eliminar tareas, así como exportar la lista de tareas a un archivo Excel o JSON e importar tareas desde un archivo JSON.

## Requisitos

Para ejecutar esta aplicación, necesitarás tener instalado lo siguiente:

- Python: Asegúrate de tener Python 3.7 o superior.
- Dependencias de Python: Asegúrate de tener las siguientes librerías instaladas.

```bash
pip install -r requirements.txt
```

Dependencias necesarias:

```bash
makefileCopy codeSQLAlchemy==1.4.49
streamlit
pandas
openpyxl
```

## Clonar el repositorio

Para clonar el repositorio y comenzar a trabajar con la aplicación, sigue estos pasos:

1. Abre tu terminal y navega hasta la carpeta donde quieres clonar el repositorio.
2. Ejecuta el siguiente comando para clonar el repositorio:

```bash
git clone https://github.com/Mizamarzes/gestion-tareas-python.git
```

1. Entra en el directorio del proyecto:

```bash
cd gestion-tareas-python
```

1. Instala las dependencias del proyecto:

```bash
pip install -r requirements.txt
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

  

  ![ui-create-task](D:\code\beca-ia-campuslands\gestion-tareas-python\img\ui-create-task.PNG)

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
    - **⚙**: Permite actualizar los detalles de la tarea(en desarrollo).

![ui-tasklist](D:\code\beca-ia-campuslands\gestion-tareas-python\img\ui-tasklist.PNG)

### 3. **Exportar tareas a Excel**

- En la sección **"Export Tasks to Excel"**, puedes hacer clic en el botón **"Export to Excel"**.
- Esto generará un archivo Excel con la lista de tareas.
- Una vez generado, podrás descargar el archivo haciendo clic en el botón **"Download Excel File"**.

![excel-example-data](D:\code\beca-ia-campuslands\gestion-tareas-python\img\excel-example-data.PNG)

### 4. **Exportar tareas a JSON**

- En la sección **"Export Tasks to JSON"**, puedes hacer clic en el botón **"Export to JSON"**.
- Esto generará un archivo JSON con la lista de tareas.
- Una vez generado, podrás descargar el archivo haciendo clic en el botón **"Download JSON File"**.

![json-example-data](D:\code\beca-ia-campuslands\gestion-tareas-python\img\json-example-data.PNG)

### 5. **Importar tareas desde un archivo JSON**

- En la sección **"Import Tasks from JSON"**, podrás seleccionar un archivo JSON que contenga tareas.
- Haz clic en el botón **"Upload JSON File"** para cargar el archivo.
- Una vez cargado, las tareas se agregarán a la lista y podrás verlas en la sección de tareas.

![ui-import-export](D:\code\beca-ia-campuslands\gestion-tareas-python\img\ui-import-export.PNG)

## Estructura del Proyecto

La estructura del proyecto es la siguiente:

![file-structure](D:\code\beca-ia-campuslands\gestion-tareas-python\img\file-structure.PNG)

## SonarQube - Análisis de Calidad de Código

Para mantener la calidad del código, se utiliza SonarQube para realizar un análisis estático. A continuación, puedes ver un resumen del análisis realizado:

![sonarqube-overview](D:\code\beca-ia-campuslands\gestion-tareas-python\img\sonarqube-overview.PNG)