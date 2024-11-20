import speedtest  # Para medir velocidad de carga y descarga
import requests   # Para medir tiempos de carga de páginas
import subprocess # Para usar ping y calcular latencia y pérdida de paquetes
import time
import statistics # Para calcular promedio, máximo, y mínimo de las mediciones
from config import URLS_PRUEBA, PING_TIMEOUT, PAQUETES_PING

def medir_velocidad():
    """Realiza una prueba de velocidad de descarga y carga utilizando la API de speedtest"""
    st = speedtest.Speedtest()
    st.get_best_server()  # Selecciona el mejor servidor automáticamente
    velocidad_descarga = st.download() / 1_000_000  # Convertimos a Mbps
    velocidad_carga = st.upload() / 1_000_000       # Convertimos a Mbps
    return velocidad_descarga, velocidad_carga

def medir_latencia_jitter(url):
    """Calcula latencia y jitter mediante ping a una URL o dirección IP"""
    latencias = []
    
    for _ in range(PAQUETES_PING):
        ping_result = subprocess.run(
            ["ping", "-c", "1", "-W", str(PING_TIMEOUT), url],
            capture_output = True,
            text = True
        )
        
        if "time=" in ping_result.stdout:
            time_str = ping_result.stdout.split("time=")[1].split(" ")[0]
            latencias.append(float(time_str))
    
    if len(latencias) > 1:
        latencia_promedio = statistics.mean(latencias)
        jitter = statistics.stdev(latencias) if len(latencias) > 1 else 0
    else:
        latencia_promedio, jitter = None, None  # Si no se lograron pings exitosos
    
    return latencia_promedio, jitter

def medir_perdida(url):
    """Calcula el porcentaje de pérdida de paquetes mediante ping a una URL o IP"""
    ping_result = subprocess.run(
        ["ping", "-c", str(PAQUETES_PING), "-W", str(PING_TIMEOUT), url],
        capture_output=True,
        text=True
    )
    
    if "received" in ping_result.stdout:
        paquetes_enviados = int(ping_result.stdout.split("transmitted")[0].strip())
        paquetes_recibidos = int(ping_result.stdout.split(",")[1].strip().split()[0])
        perdida = ((paquetes_enviados - paquetes_recibidos) / paquetes_enviados) * 100
    else:
        perdida = None  # Indica que no se pudo realizar la prueba correctamente
    
    return perdida

def medir_tiempo_carga(url):
    """Calcula el tiempo de carga de una página web"""
    inicio = time.time()
    try:
        response = requests.get(url, timeout=PING_TIMEOUT)
        tiempo_carga = time.time() - inicio
        if response.status_code != 200:
            tiempo_carga = None  # Indica un error en la carga
    except requests.exceptions.RequestException:
        tiempo_carga = None  # Error en la conexión
    return tiempo_carga

def realizar_mediciones():
    """Realiza todas las mediciones para cada URL y retorna los resultados"""
    resultados = []
    
    for url in URLS_PRUEBA:
        print(f"Iniciando medición para: {url}")
        
        # Medición de velocidad
        velocidad_descarga, velocidad_carga = medir_velocidad()
        
        # Medición de latencia y jitter
        latencia, jitter = medir_latencia_jitter(url)
        
        # Medición de pérdida de paquetes
        perdida = medir_perdida(url)
        
        # Medición de tiempo de carga
        tiempo_carga = medir_tiempo_carga(url)
        
        resultados.append({
            "url": url,
            "velocidad_descarga": velocidad_descarga,
            "velocidad_carga": velocidad_carga,
            "latencia": latencia,
            "jitter": jitter,
            "perdida": perdida,
            "tiempo_carga": tiempo_carga
        })
        
        print(f"Mediciones completadas para: {url}")
    
    return resultados

def realizar_prueba():
    """Realiza una prueba completa de QoS y QoE en cada URL de prueba configurada en config.py"""
    # Inicializamos un diccionario para almacenar los resultados de cada URL
    resultados_finales = {}

    # Iteramos a través de cada URL en la configuración para medir cada parámetro
    for url in URLS_PRUEBA:
        print(f"\nIniciando prueba para: {url}")
        
        # Medir velocidad de descarga y carga
        print("Midiendo velocidad...")
        velocidad_descarga, velocidad_carga = medir_velocidad()
        
        # Medir latencia y jitter
        print("Midiendo latencia y jitter...")
        latencia, jitter = medir_latencia_jitter(url)
        
        # Medir pérdida de paquetes
        print("Midiendo pérdida de paquetes...")
        perdida = medir_perdida(url)
        
        # Medir tiempo de carga de la página
        print("Midiendo tiempo de carga de la página...")
        tiempo_carga = medir_tiempo_carga(url)
        
        # Agregamos los resultados de la URL actual al diccionario de resultados finales
        resultados_finales[url] = {
            "velocidad_descarga (Mbps)": velocidad_descarga,
            "velocidad_carga (Mbps)": velocidad_carga,
            "latencia (ms)": latencia,
            "jitter (ms)": jitter,
            "pérdida de paquetes (%)": perdida,
            "tiempo_carga (s)": tiempo_carga
        }

        print(f"Prueba completada para: {url}")

    # Retornamos el diccionario con los resultados de cada URL
    return resultados_finales