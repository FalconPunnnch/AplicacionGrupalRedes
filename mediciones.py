# mediciones.py

import random
import time

def realizar_prueba(url):
    """Simula la realización de una prueba de QoS/QoE para una URL."""
    
    # Simulación de tiempos de medición
    tiempo_total = random.uniform(10, 60)  # Simulación de un tiempo total de prueba
    velocidad_descarga = random.uniform(10, 100)  # Mbps
    velocidad_carga = random.uniform(5, 50)  # Mbps
    velocidad_pico = random.uniform(50, 150)  # Mbps
    velocidad_suelo = random.uniform(5, 10)  # Mbps
    latencia = random.uniform(20, 100)  # ms
    jitter = random.uniform(0, 10)  # ms
    perdida_paquetes = random.uniform(0, 1)  # Porcentaje
    momento = "mañana"  # Ejemplo de momento
    dispositivo = "PC"  # Ejemplo de dispositivo

    # Crear el resultado como un diccionario
    resultado = {
        'url': url,
        'velocidad_descarga': velocidad_descarga,
        'velocidad_carga': velocidad_carga,
        'velocidad_pico': velocidad_pico,
        'velocidad_suelo': velocidad_suelo,
        'latencia': latencia,
        'jitter': jitter,
        'perdida_paquetes': perdida_paquetes,
        'tiempo_total': tiempo_total,
        'momento': momento,
        'dispositivo': dispositivo
    }
    
    # Retornar el resultado
    return resultado
