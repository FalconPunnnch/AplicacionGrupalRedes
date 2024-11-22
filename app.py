# app.py

import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import config
from mediciones import realizar_prueba
from data_storage import crear_conexion, crear_tablas, almacenar_resultado, obtener_resultados, limpiar_cache


class Aplicacion:
    def __init__(self, master):
        self.master = master
        self.master.title("Aplicación de Medición QoS y QoE")
        self.master.geometry("500x400")

        self.resultados = []

        # Titulo de la ventana
        self.titulo_label = tk.Label(self.master, text="Medición de QoS y QoE", font=("Arial", 18))
        self.titulo_label.pack(pady=20)

        # Botón para realizar una prueba
        self.boton_realizar_prueba = tk.Button(self.master, text="Realizar Prueba", command=self.realizar_prueba)
        self.boton_realizar_prueba.pack(pady=10)

        # Botón para ver resultados de las pruebas
        self.boton_ver_resultados = tk.Button(self.master, text="Ver Resultados", command=self.ver_resultados)
        self.boton_ver_resultados.pack(pady=10)

        # Botón para generar un informe
        self.boton_generar_informe = tk.Button(self.master, text="Generar Informe", command=self.generar_informe)
        self.boton_generar_informe.pack(pady=10)

        # Botón para programar una prueba
        self.boton_programar_prueba = tk.Button(self.master, text="Programar Prueba", command=self.programar_prueba)
        self.boton_programar_prueba.pack(pady=10)

        # Botón para limpiar caché
        self.boton_limpiar_cache = tk.Button(self.master, text="Limpiar Caché", command=self.limpiar_cache)
        self.boton_limpiar_cache.pack(pady=10)
        
        # Crear conexión a la base de datos y tablas
        self.conexion = crear_conexion()
        crear_tablas(self.conexion)

        
    def realizar_prueba(self):
        # Realiza una prueba de medición
        resultado = realizar_prueba("https://www.youtube.com")
        self.resultados.append(resultado)

        # Guarda el resultado en la base de datos
        almacenar_resultado(self.conexion, resultado)

        # Notifica al usuario
        messagebox.showinfo("Resultado", "Prueba realizada y guardada exitosamente.")

    def ver_resultados(self):
        # Obtiene resultados desde la base de datos
        resultados_db = obtener_resultados(self.conexion)
        
        if not resultados_db:
            messagebox.showwarning("Sin resultados", "No hay resultados de pruebas almacenados.")
            return

        # Mostrar resultados de las pruebas almacenadas
        resultados_texto = "\n".join([f"ID {r[0]}: {r[1]}, {r[2]} Mbps, {r[5]} ms" for r in resultados_db])
        messagebox.showinfo("Resultados", resultados_texto)

    def generar_informe(self):
        if not self.resultados:
            messagebox.showwarning("Sin resultados", "No hay resultados para generar un informe.")
            return

        # Generar un informe de los resultados
        fecha_actual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        archivo_informe = f"Informe_{fecha_actual}.txt"
        with open(archivo_informe, "w") as f:
            for resultado in self.resultados:
                f.write(f"{resultado}\n")
        messagebox.showinfo("Informe generado", f"Informe guardado como {archivo_informe}")

    def programar_prueba(self):
        # Programar una prueba según la configuración de hora
        hora_programada = config.PROGRAMACION_PRUEBAS["mañana"]  # Simplemente elige un valor de ejemplo
        messagebox.showinfo("Prueba Programada", f"Prueba programada para {hora_programada}")

    def limpiar_cache(self):
        """Elimina todos los resultados almacenados en la base de datos."""
        conexion = crear_conexion()
        if not conexion:
            messagebox.showwarning("Error", "No se pudo establecer la conexión con la base de datos.")
            return
        
        limpiar_cache(conexion)
        conexion.close()

        messagebox.showinfo("Caché Limpiada", "Los resultados han sido eliminados exitosamente.")



def main():
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()


if __name__ == "__main__":
    main()