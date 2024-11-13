import os
import csv
from datetime import datetime

def generar_reporte(resultados_comparativos):
    """Genera un reporte en texto y CSV con los resultados comparativos."""
    
    # Crear la carpeta para los reportes si no existe
    if not os.path.exists('reportes'):
        os.makedirs('reportes')

    # Nombre del archivo con la fecha y hora
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    reporte_txt = f'reportes/reporte_comparativo_{timestamp}.txt'
    reporte_csv = f'reportes/reporte_comparativo_{timestamp}.csv'
    
    # Generar reporte en formato texto
    with open(reporte_txt, 'w') as file:
        file.write(f"Reporte Comparativo de Resultados de QoS y QoE\n")
        file.write(f"Fecha y Hora: {timestamp}\n\n")
        
        for url, stats in resultados_comparativos.items():
            file.write(f"Resultados para {url}:\n")
            for metrica, valores in stats.items():
                file.write(f"  {metrica.capitalize()}:\n")
                file.write(f"    Promedio: {valores['promedio']:.2f}\n")
                file.write(f"    Mediana: {valores['mediana']:.2f}\n")
                file.write(f"    Desviación estándar: {valores['desviacion_estandar']:.2f}\n")
                file.write(f"    Máximo: {valores['maximo']:.2f}\n")
                file.write(f"    Mínimo: {valores['minimo']:.2f}\n")
            file.write("\n")
    
    print(f"Reporte en formato texto generado: {reporte_txt}")
    
    # Generar reporte en formato CSV
    with open(reporte_csv, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["URL", "Métrica", "Promedio", "Mediana", "Desviación Estándar", "Máximo", "Mínimo"])

        for url, stats in resultados_comparativos.items():
            for metrica, valores in stats.items():
                writer.writerow([
                    url,
                    metrica.capitalize(),
                    f"{valores['promedio']:.2f}",
                    f"{valores['mediana']:.2f}",
                    f"{valores['desviacion_estandar']:.2f}",
                    f"{valores['maximo']:.2f}",
                    f"{valores['minimo']:.2f}",
                ])
    
    print(f"Reporte en formato CSV generado: {reporte_csv}")

def mostrar_reporte(resultados_comparativos):
    """Muestra un resumen de los resultados comparativos por consola."""
    for url, stats in resultados_comparativos.items():
        print(f"\nResumen de Resultados para {url}:")
        for metrica, valores in stats.items():
            print(f"  {metrica.capitalize()}:")
            print(f"    Promedio: {valores['promedio']:.2f}")
            print(f"    Mediana: {valores['mediana']:.2f}")
            print(f"    Desviación estándar: {valores['desviacion_estandar']:.2f}")
            print(f"    Máximo: {valores['maximo']:.2f}")
            print(f"    Mínimo: {valores['minimo']:.2f}")