import platform
import psutil
import socket

def obtener_informacion_dispositivo():
    """Obtiene información básica sobre el dispositivo."""
    info_dispositivo = {
        "nombre_dispositivo": socket.gethostname(),  # Nombre del dispositivo (hostname)
        "sistema_operativo": platform.system(),      # Sistema operativo (Windows, Linux, macOS)
        "version_so": platform.version(),           # Versión del sistema operativo
        "arquitectura": platform.architecture()[0], # Arquitectura del procesador (32-bit, 64-bit)
        "procesador": platform.processor(),         # Nombre del procesador
        "memoria_total": psutil.virtual_memory().total,  # Memoria RAM total (en bytes)
        "memoria_disponible": psutil.virtual_memory().available,  # Memoria disponible (en bytes)
        "cpu_percent": psutil.cpu_percent(interval=1), # Porcentaje de uso de la CPU
        "cpu_count": psutil.cpu_count(logical=False), # Número de núcleos físicos de la CPU
        "cpu_logical_count": psutil.cpu_count(logical=True), # Número total de núcleos lógicos
    }
    
    return info_dispositivo

def mostrar_info_dispositivo(info_dispositivo):
    """Muestra la información del dispositivo en consola."""
    print("Información del dispositivo:")
    print(f"Nombre del dispositivo: {info_dispositivo['nombre_dispositivo']}")
    print(f"Sistema operativo: {info_dispositivo['sistema_operativo']} {info_dispositivo['version_so']}")
    print(f"Arquitectura: {info_dispositivo['arquitectura']}")
    print(f"Procesador: {info_dispositivo['procesador']}")
    print(f"Memoria RAM total: {info_dispositivo['memoria_total'] / (1024 ** 3):.2f} GB")
    print(f"Memoria RAM disponible: {info_dispositivo['memoria_disponible'] / (1024 ** 3):.2f} GB")
    print(f"Uso de CPU: {info_dispositivo['cpu_percent']}%")
    print(f"Número de núcleos físicos de CPU: {info_dispositivo['cpu_count']}")
    print(f"Número de núcleos lógicos de CPU: {info_dispositivo['cpu_logical_count']}")

if __name__ == '__main__':
    # Obtener la información del dispositivo
    info_dispositivo = obtener_informacion_dispositivo()
    
    # Mostrar la información en consola
    mostrar_info_dispositivo(info_dispositivo)