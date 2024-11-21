import tkinter as tk
from tkinter import messagebox
from measurement import realizar_prueba
from scheduler import programar_prueba
from report_generator import generar_informe
from data_storage import guardar_resultado
from datetime import datetime
import config

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

    def realizar_prueba(self):
        # Aquí se debe realizar una prueba de medición
        resultado = realizar_prueba("https://example.com")
        self.resultados.append(resultado)
        messagebox.showinfo("Resultado", "Prueba realizada exitosamente.")

    def ver_resultados(self):
        if not self.resultados:
            messagebox.showwarning("Sin resultados", "No hay resultados de pruebas.")
            return
        
        # Mostrar resultados de las pruebas realizadas
        resultados_texto = "\n".join([str(r) for r in self.resultados])
        messagebox.showinfo("Resultados", resultados_texto)

    def generar_informe(self):
        if not self.resultados:
            messagebox.showwarning("Sin resultados", "No hay resultados para generar un informe.")
            return
        
        # Generar un informe de los resultados
        fecha_actual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        archivo_informe = f"Informe_{fecha_actual}.txt"
        generar_informe(self.resultados, archivo_informe)
        messagebox.showinfo("Informe generado", f"Informe guardado como {archivo_informe}")

    def programar_prueba(self):
        # Programar una prueba según la configuración de hora
        hora_programada = programar_prueba(config.PROGRAMACION_PRUEBAS)
        messagebox.showinfo("Prueba Programada", f"Prueba programada para {hora_programada}")


def main():
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()


if __name__ == "__main__":
    main()