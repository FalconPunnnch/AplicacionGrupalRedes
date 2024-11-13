import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random  # Solo para simular datos; en producción, usaremos los datos de `measurement.py`
from measurement import realizar_mediciones  # Importamos las mediciones
from config import CANTIDAD_DE_PRUEBAS, INTERVALO_ENTRE_PRUEBAS, URLS_PRUEBA  # Importamos configuraciones

# Inicialización de datos
data_velocidad_descarga = []
data_velocidad_carga = []
data_latencia = []
data_jitter = []
data_perdida = []

def actualizar_datos():
    """Función para obtener nuevos datos de mediciones y almacenarlos en las listas de datos."""
    resultados = realizar_mediciones()
    
    for resultado in resultados:
        # Agregamos datos a cada lista correspondiente
        data_velocidad_descarga.append(resultado['velocidad_descarga'])
        data_velocidad_carga.append(resultado['velocidad_carga'])
        data_latencia.append(resultado['latencia'])
        data_jitter.append(resultado['jitter'])
        data_perdida.append(resultado['perdida'])
        
        # Mantenemos un máximo de `CANTIDAD_DE_PRUEBAS` datos en el gráfico
        if len(data_velocidad_descarga) > CANTIDAD_DE_PRUEBAS:
            data_velocidad_descarga.pop(0)
            data_velocidad_carga.pop(0)
            data_latencia.pop(0)
            data_jitter.pop(0)
            data_perdida.pop(0)

def configurar_graficos():
    """Configura los gráficos de Matplotlib para la visualización en tiempo real."""
    fig, axs = plt.subplots(3, 1, figsize=(10, 8))
    fig.suptitle("Mediciones de QoS y QoE en tiempo real")

    # Configuración de subgráficos
    def init():
        for ax in axs:
            ax.clear()
        axs[0].set_title("Velocidad de Descarga y Carga (Mbps)")
        axs[1].set_title("Latencia y Jitter (ms)")
        axs[2].set_title("Pérdida de Paquetes (%)")
        axs[0].legend(["Velocidad Descarga", "Velocidad Carga"], loc="upper right")
        axs[1].legend(["Latencia", "Jitter"], loc="upper right")
        axs[2].legend(["Pérdida de Paquetes"], loc="upper right")
        
    def actualizar_graficos(frame):
        actualizar_datos()  # Actualizamos los datos con nuevas mediciones
        
        # Actualización de gráficos con los datos actuales
        axs[0].clear()
        axs[0].plot(data_velocidad_descarga, color="blue")
        axs[0].plot(data_velocidad_carga, color="green")
        axs[0].set_ylabel("Mbps")
        
        axs[1].clear()
        axs[1].plot(data_latencia, color="red")
        axs[1].plot(data_jitter, color="purple")
        axs[1].set_ylabel("ms")
        
        axs[2].clear()
        axs[2].plot(data_perdida, color="orange")
        axs[2].set_ylabel("%")
        
        # Ajuste de ejes y etiquetas
        init()
    
    ani = FuncAnimation(fig, actualizar_graficos, init_func=init, interval=INTERVALO_ENTRE_PRUEBAS * 1000)
    plt.tight_layout()
    plt.show()

def iniciar_graficos():
    """Función principal para iniciar la visualización de gráficos en tiempo real."""
    configurar_graficos()