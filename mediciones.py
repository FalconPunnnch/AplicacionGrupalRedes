import speedtest
import time
import ping3

def realizar_prueba(url):
    """Realiza una prueba real de QoS/QoE utilizando speedtest-cli y ping3 para una URL."""
    
    # Realizar la prueba de velocidad utilizando speedtest-cli
    st = speedtest.Speedtest()
    st.get_best_server()

    # Realizar las mediciones
    velocidad_descarga = st.download() / 1_000_000  # Convertir de bps a Mbps
    velocidad_carga = st.upload() / 1_000_000  # Convertir de bps a Mbps
    latencia = st.results.ping  # Latencia en ms
    velocidad_pico = velocidad_descarga  # En este caso, se utiliza la velocidad de descarga como pico
    velocidad_suelo = velocidad_carga  # Se asume que la velocidad de carga es el "suelo"
    
    # Medir jitter y pérdida de paquetes utilizando ping3
    # Hacer ping a la URL para obtener jitter y pérdida de paquetes
    host = url  # Suponiendo que url es un dominio como 'google.com' o 'youtube.com'
    
    # Realizar varios pings para obtener una muestra
    ping_results = []
    for _ in range(10):  # Realizar 10 pings
        delay = ping3.ping(host)
        if delay is not None:
            ping_results.append(delay)
    
    # Calcular jitter (desviación estándar de los pings)
    if len(ping_results) > 1:
        jitter = round(max(ping_results) - min(ping_results), 2)  # Diferencia entre el ping máximo y mínimo como jitter
    else:
        jitter = 0  # Si no hay suficientes pings, se establece a 0

    # Calcular la pérdida de paquetes
    perdida_paquetes = 100 * (10 - len(ping_results)) / 10  # Porcentaje de paquetes perdidos (basado en los 10 pings)

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
        'tiempo_total': time.time(),  # Establecer el tiempo total como el tiempo de ejecución
        'dispositivo': dispositivo
    }
    
    # Retornar el resultado
    return resultado
