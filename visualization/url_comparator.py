from measurement import realizar_mediciones
from config import URLS_PRUEBA, CANTIDAD_DE_PRUEBAS
import statistics

def comparar_urls():
    """Función principal para realizar mediciones y comparar URLs en base a QoS y QoE."""
    resultados_comparativos = {}

    for url in URLS_PRUEBA:
        print(f"Realizando mediciones para {url}...")

        # Realizamos varias mediciones para cada URL y guardamos los resultados
        mediciones_url = [realizar_mediciones(url) for _ in range(CANTIDAD_DE_PRUEBAS)]
        
        # Extracción y cálculo de estadísticas para cada métrica
        resultados_comparativos[url] = {
            "velocidad_descarga": calcular_estadisticas([m['velocidad_descarga'] for m in mediciones_url]),
            "velocidad_carga": calcular_estadisticas([m['velocidad_carga'] for m in mediciones_url]),
            "latencia": calcular_estadisticas([m['latencia'] for m in mediciones_url]),
            "jitter": calcular_estadisticas([m['jitter'] for m in mediciones_url]),
            "perdida": calcular_estadisticas([m['perdida'] for m in mediciones_url]),
        }

    mostrar_resultados(resultados_comparativos)

def calcular_estadisticas(datos):
    """Calcula estadísticas de interés sobre una lista de datos."""
    return {
        "promedio": statistics.mean(datos),
        "mediana": statistics.median(datos),
        "desviacion_estandar": statistics.stdev(datos) if len(datos) > 1 else 0,
        "maximo": max(datos),
        "minimo": min(datos)
    }

def mostrar_resultados(resultados):
    """Muestra los resultados comparativos en formato amigable."""
    for url, stats in resultados.items():
        print(f"\nResultados para {url}:")
        for metrica, valores in stats.items():
            print(f"  {metrica.capitalize()}:")
            print(f"    Promedio: {valores['promedio']:.2f}")
            print(f"    Mediana: {valores['mediana']:.2f}")
            print(f"    Desviación estándar: {valores['desviacion_estandar']:.2f}")
            print(f"    Máximo: {valores['maximo']:.2f}")
            print(f"    Mínimo: {valores['minimo']:.2f}")

def ejecutar_comparacion():
    """Función para ejecutar la comparación de URLs en base a mediciones."""
    comparar_urls()