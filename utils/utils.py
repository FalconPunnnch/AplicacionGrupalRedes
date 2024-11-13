import json
import os
from datetime import datetime

def guardar_json(data, file_path):
    """Guarda los datos en un archivo JSON."""
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Datos guardados correctamente en {file_path}")
    except Exception as e:
        print(f"Error al guardar el archivo JSON: {e}")

def cargar_json(file_path):
    """Carga los datos desde un archivo JSON."""
    if not os.path.exists(file_path):
        print(f"El archivo {file_path} no existe.")
        return None
    
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(f"Error al cargar el archivo JSON: {e}")
        return None

def obtener_fecha_actual():
    """Devuelve la fecha y hora actual en formato 'YYYY-MM-DD HH:MM:SS'."""
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def convertir_a_gb(bytes_value):
    """Convierte valores en bytes a gigabytes (GB)."""
    return bytes_value / (1024 ** 3)

def log_error(mensaje, file_path="error_log.txt"):
    """Registra un mensaje de error en un archivo de log."""
    fecha_actual = obtener_fecha_actual()
    try:
        with open(file_path, 'a') as f:
            f.write(f"{fecha_actual} - {mensaje}\n")
    except Exception as e:
        print(f"Error al guardar el log: {e}")

def generar_nombre_archivo(tipo="informe"):
    """Genera un nombre de archivo único para informes o logs basados en la fecha y hora actual."""
    fecha_actual = obtener_fecha_actual().replace(":", "-").replace(" ", "_")
    return f"{tipo}_{fecha_actual}.txt"

def formatear_bytes(bytes_value):
    """Formatea valores en bytes a un formato legible (GB, MB, KB)."""
    if bytes_value >= (1024 ** 3):
        return f"{bytes_value / (1024 ** 3):.2f} GB"
    elif bytes_value >= (1024 ** 2):
        return f"{bytes_value / (1024 ** 2):.2f} MB"
    elif bytes_value >= 1024:
        return f"{bytes_value / 1024:.2f} KB"
    else:
        return f"{bytes_value} bytes"

if __name__ == '__main__':
    # Ejemplos de uso
    datos = {"url": "https://example.com", "velocidad_descarga": 50}
    file_path = "datos_prueba.json"
    guardar_json(datos, file_path)

    datos_cargados = cargar_json(file_path)
    print(datos_cargados)

    print(obtener_fecha_actual())
    print(convertir_a_gb(1073741824))  # Ejemplo con 1 GB
    print(formatear_bytes(1048576))  # Ejemplo con 1 MB

    log_error("Este es un mensaje de prueba para el log.")
    print(generar_nombre_archivo("reporte"))