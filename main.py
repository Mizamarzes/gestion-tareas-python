from models.model import init_db
import os

def inicializar_aplicacion():
    # Crear la base de datos si no existe
    init_db()
    print("Base de datos inicializada.")

if __name__ == "__main__":
    inicializar_aplicacion()

    # Opcional: Ejecutar el servidor de Streamlit desde Python
    os.system("streamlit run app.py")
