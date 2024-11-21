import sqlite3
from sqlite3 import Error
import os

# Ruta al archivo de la base de datos
DB_PATH = 'mediciones.db'

def crear_conexion():
    """Crea una conexión con la base de datos SQLite."""
    conexion = None
    try:
        conexion = sqlite3.connect(DB_PATH)
        print(f"Conexión exitosa a la base de datos {DB_PATH}")
    except Error as e:
        print(f"Error al conectar con la base de datos: {e}")
    return conexion

def crear_tablas(conexion):
    """Crea las tablas necesarias para almacenar los resultados de las mediciones."""
    try:
        cursor = conexion.cursor()
        # Crear tabla para almacenar resultados de las pruebas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS resultados (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT NOT NULL,
                velocidad_descarga REAL,
                velocidad_carga REAL,
                velocidad_pico REAL,
                velocidad_suelo REAL,
                latencia REAL,
                jitter REAL,
                perdida_paquetes REAL,
                tiempo_total REAL,
                momento TEXT,
                dispositivo TEXT,
                fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        ''')
        # Crear tabla para almacenar configuraciones
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS configuracion (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cantidad_de_pruebas INTEGER,
                intervalo_entre_pruebas INTEGER,
                programacion_pruebas TEXT
            );
        ''')
        conexion.commit()
        print("Tablas creadas o verificadas correctamente.")
    except Error as e:
        print(f"Error al crear las tablas: {e}")

def almacenar_resultado(conexion, resultado):
    """Almacena los resultados de una prueba en la base de datos."""
    try:
        cursor = conexion.cursor()
        query = '''
            INSERT INTO resultados (url, velocidad_descarga, velocidad_carga, velocidad_pico, velocidad_suelo,
                                    latencia, jitter, perdida_paquetes, tiempo_total, momento, dispositivo)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        '''
        cursor.execute(query, (resultado['url'], resultado['velocidad_descarga'], resultado['velocidad_carga'],
                               resultado['velocidad_pico'], resultado['velocidad_suelo'], resultado['latencia'],
                               resultado['jitter'], resultado['perdida_paquetes'], resultado['tiempo_total'],
                               resultado['momento'], resultado['dispositivo']))
        conexion.commit()
        print(f"Resultado almacenado para la URL: {resultado['url']}")
    except Error as e:
        print(f"Error al almacenar el resultado: {e}")

def obtener_resultados(conexion):
    """Obtiene todos los resultados almacenados en la base de datos."""
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM resultados;")
        resultados = cursor.fetchall()
        return resultados
    except Error as e:
        print(f"Error al obtener los resultados: {e}")
        return []

def almacenar_configuracion(conexion, configuracion):
    """Almacena la configuración de la aplicación en la base de datos."""
    try:
        cursor = conexion.cursor()
        query = '''
            INSERT INTO configuracion (cantidad_de_pruebas, intervalo_entre_pruebas, programacion_pruebas)
            VALUES (?, ?, ?);
        '''
        cursor.execute(query, (configuracion['cantidad_de_pruebas'], configuracion['intervalo_entre_pruebas'],
                               str(configuracion['programacion_pruebas'])))
        conexion.commit()
        print("Configuración almacenada correctamente.")
    except Error as e:
        print(f"Error al almacenar la configuración: {e}")

def obtener_configuracion(conexion):
    """Obtiene la configuración almacenada en la base de datos."""
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM configuracion ORDER BY id DESC LIMIT 1;")
        configuracion = cursor.fetchone()
        return configuracion
    except Error as e:
        print(f"Error al obtener la configuración: {e}")
        return None

def cerrar_conexion(conexion):
    """Cierra la conexión con la base de datos."""
    if conexion:
        conexion.close()
        print("Conexión cerrada correctamente.")

# Ejemplo de uso
if __name__ == '__main__':
    # Crear conexión
    conexion = crear_conexion()
    
    # Crear tablas si no existen
    crear_tablas(conexion)
    
    # Ejemplo de almacenar configuración
    configuracion = {
        'cantidad_de_pruebas': 3,
        'intervalo_entre_pruebas': 60,
        'programacion_pruebas': {
            "mañana": "06:00",
            "tarde": "12:00",
            "noche": "19:00"
        }
    }
    almacenar_configuracion(conexion, configuracion)

    # Ejemplo de almacenar resultados
    resultado = {
        'url': 'https://www.example.com',
        'velocidad_descarga': 15.5,
        'velocidad_carga': 5.2,
        'velocidad_pico': 20.0,
        'velocidad_suelo': 10.0,
        'latencia': 50.0,
        'jitter': 5.0,
        'perdida_paquetes': 0.0,
        'tiempo_total': 30.0,
        'momento': 'mañana',
        'dispositivo': 'PC'
    }
    almacenar_resultado(conexion, resultado)
    
    # Obtener y mostrar resultados
    resultados = obtener_resultados(conexion)
    for r in resultados:
        print(r)
    
    # Cerrar conexión
    cerrar_conexion(conexion)

def guardar_resultado(resultado):
    """
    Guarda un resultado de prueba en la base de datos.
    :param resultado: Diccionario con los datos del resultado.
    """
    conexion = crear_conexion()
    if not conexion:
        print("No se pudo establecer la conexión con la base de datos.")
        return
    
    try:
        almacenar_resultado(conexion, resultado)
        print(f"Resultado guardado exitosamente: {resultado}")
    except Error as e:
        print(f"Error al guardar el resultado: {e}")
    finally:
        cerrar_conexion(conexion)
