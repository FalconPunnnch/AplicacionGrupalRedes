import os
from datetime import datetime

# URLs a probar
URLS_PRUEBA = [
    "https://www.netflix.com",
    "https://www.youtube.com",
    "https://play.pokemonshowdown.com",
    "https://ulima.blackboard.com",
]

# Configuración del servidor de Speedtest
# Speedtest CLI selecciona el servidor más cercano automáticamente,
# pero también puedes definir un servidor específico si tienes un ID
# (debes obtener el ID del servidor de Speedtest deseado).
SPEEDTEST_SERVER_ID = None  # Define un ID específico o deja None para el más cercano

# Parámetros de prueba
CANTIDAD_DE_PRUEBAS = 3
INTERVALO_ENTRE_PRUEBAS = 60      # En segundos
PROGRAMACION_PRUEBAS = {
    "mañana": "06:00",
    "tarde": "12:00",
    "noche": "19:00",
}

# Parámetros de red
PING_TIMEOUT = 2                   # Tiempo de espera en segundos
PAQUETES_PING = 4                  # Para latencia promedio
TAMAÑO_JITTER = 10                 # Número de muestras
PAQUETES_PERDIDA = 10              # Número de paquetes para medir pérdida de datos

# Configuración de gráficos en tiempo real
GRAFICOS_ACTUALIZACION_INTERVALO = 1  # Tiempo en segundos para actualizar los gráficos en tiempo real

# Configuración de la base de datos
DB_PATH = "data/results.db"        # Ruta de la base de datos SQLite para almacenar resultados

# Configuración de generación de informes
INFORMES_PATH = "reports/"         # Carpeta donde se guardarán los informes generados en PDF
FORMATO_FECHA = "%Y-%m-%d %H:%M:%S"  # Formato de fecha y hora para los informes

# Opciones de visualización para comparar URLs
COMPARACION_METRICAS = [
    "velocidad_descarga", "velocidad_carga", "latencia", "jitter", "pérdida_paquetes"
]  # Métricas a mostrar en la comparación
