# QoLab: un aplicativo para la medición de parámetros de QoS y QoE.
## Proyecto Integrador grupal para el curso de Redes de Computadoras de la Universidad de Lima.
### Profesor: Jim Dios Luna.
### Integrantes: Cristian Erazo Mena, Alejandra Falcon Flores, Ricardo Llallico Cruz, Gabriel Saez Olin.

### Funcionalidades principales implementadas:

1. Medición de QoS y QoE en tiempo real: Calcular las métricas de rendimiento para cada sitio web (tiempo de carga, latencia, ancho de banda, jitter, porcentaje de pérdida de paquetes, velocidad de carga y descarga).
2. Gráficos en tiempo real: Visualizar las métricas de velocidad de carga y descarga, latencia y otras, permitiendo una comparación rápida y visual del rendimiento entre diferentes sitios web.
3. Programación de pruebas: Ejecutar pruebas en momentos específicos del día (mañana, tarde y noche) y en diferentes dispositivos para analizar variaciones en la calidad de servicio y experiencia de usuario.
4. Generación de informes de prueba: Crear reportes detallados al finalizar cada prueba, incluyendo estadísticas como velocidad promedio, pico, suelo, latencia, jitter, porcentaje de pérdida de paquetes y tiempo total de la prueba.
5. Comparación de rendimiento entre URLs: Mostrar una interfaz que permita seleccionar múltiples URLs para evaluar y comparar sus métricas en tiempo real y en diferentes condiciones.
6. Configuración de variables de control: Establecer el servidor de prueba (p. ej., un servidor de Speedtest específico) para garantizar que las pruebas sean consistentes y comparables.

### Proyecto presentado con éxito, lunes 25/11/24 clase de 10am - 1pm. Calificación: 17/20.

### Sobre los archivos:
- app.py: Punto de entrada de la aplicación.
Inicializa la interfaz gráfica, conecta con las funciones principales y maneja la lógica de navegación entre ventanas de la app.

- test.py: Simula la medición de QoS y QoE para un URL determinado, como la velocidad de descarga y carga.
Realiza una prueba para medir la velocidad de descarga, carga, latencia, jitter, etc., en una URL especificada. Guarda resultados y genera reportes.

- config.py: Almacena los parámetros de configuración de la aplicación.
Facilita el ajuste de variables de control para experimentos.

- data_storage.py: Gestiona la base de datos donde se almacenan los resultados de las pruebas y la configuración de la aplicación.
Asegura que los resultados sean recuperables para visualización posterior o análisis comparativo.
