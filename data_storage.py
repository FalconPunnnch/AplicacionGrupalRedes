# data_storage.py

import sqlite3
from sqlite3 import Error

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

def limpiar_cache(conexion):
    """Elimina todos los resultados de la base de datos."""
    try:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM resultados;")
        conexion.commit()
        print("Caché limpiada exitosamente.")
    except Error as e:
        print(f"Error al limpiar caché: {e}")
