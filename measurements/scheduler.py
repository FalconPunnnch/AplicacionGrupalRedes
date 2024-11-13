import schedule   # Para la programación de tareas
import time       # Para pausar entre cada ciclo de schedule
from datetime import datetime
from measurement import realizar_mediciones  # Importar las funciones de medición
from config import INTERVALO_PRUEBA, HORARIOS_PRUEBA, URLS_PRUEBA  # Importar configuraciones

def programar_pruebas_diarias():
    """Programa las pruebas para ejecutarse en horarios específicos cada día."""
    for horario in HORARIOS_PRUEBA:
        schedule.every().day.at(horario).do(ejecutar_prueba_completa)
        print(f"Prueba programada diariamente a las {horario}")

def programar_pruebas_periodicas():
    """Programa las pruebas para ejecutarse cada cierto intervalo en minutos."""
    schedule.every(INTERVALO_PRUEBA).minutes.do(ejecutar_prueba_completa)
    print(f"Prueba programada para ejecutarse cada {INTERVALO_PRUEBA} minutos")

def ejecutar_prueba_completa():
    """Ejecuta todas las pruebas para cada URL en los horarios programados."""
    print(f"\nEjecutando pruebas - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Ejecutar las mediciones para cada URL
    resultados = realizar_mediciones()
    
    # Mostrar los resultados (podrías guardar estos resultados en una base de datos o archivo)
    for resultado in resultados:
        print(f"\nResultados para {resultado['url']}:")
        print(f"  Velocidad de descarga: {resultado['velocidad_descarga']} Mbps")
        print(f"  Velocidad de carga: {resultado['velocidad_carga']} Mbps")
        print(f"  Latencia: {resultado['latencia']} ms")
        print(f"  Jitter: {resultado['jitter']} ms")
        print(f"  Pérdida de paquetes: {resultado['perdida']}%")
        print(f"  Tiempo de carga: {resultado['tiempo_carga']} segundos")

def iniciar_scheduler():
    """Inicia el scheduler para ejecutar las pruebas según el tipo de programación."""
    # Llama a una de las funciones de programación según tus necesidades
    if HORARIOS_PRUEBA:
        programar_pruebas_diarias()
    elif INTERVALO_PRUEBA:
        programar_pruebas_periodicas()
    
    print("Scheduler iniciado. Esperando próxima ejecución de tareas...")

    # Ciclo principal del scheduler
    while True:
        schedule.run_pending()  # Ejecuta las tareas pendientes
        time.sleep(1)           # Espera antes del siguiente ciclo