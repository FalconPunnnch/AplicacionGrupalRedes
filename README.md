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

### Proyecto en desarrollo, clase de 10am - 1pm. Calificación: ?/20.

### Sobre los archivos:
- main.py: Punto de entrada de la aplicación.
Inicializa la interfaz gráfica, conecta con las funciones principales y maneja la lógica de navegación entre ventanas de la app.

- measurement.py: Contiene las funciones para medir las métricas de QoS y QoE (latencia, jitter, velocidad de carga/descarga, pérdida de paquetes).
Utiliza bibliotecas para conexión de red (como requests y socket) para realizar pruebas de rendimiento en sitios web seleccionados.

- realtime_graphs.py: Genera y actualiza gráficos en tiempo real de velocidad de carga y descarga, latencia y otras métricas.
Implementa herramientas de visualización como matplotlib o plotly para mostrar gráficos de actualización en vivo.

- scheduler.py: Permite programar la ejecución de pruebas en momentos específicos del día (mañana, tarde, noche).
Incluye lógica para realizar varias repeticiones y obtener promedios de las métricas.

- report_generator.py: Genera reportes finales en formatos como PDF o CSV al finalizar cada prueba, con todas las estadísticas relevantes.
Contiene funciones para almacenar o exportar los datos recopilados para su posterior análisis.

- url_comparator.py: Compara las métricas de diferentes URLs en función de las pruebas realizadas.
Contiene funciones que permiten seleccionar varias URLs y visualizar sus estadísticas en un solo gráfico o tabla comparativa.

- config.py: Almacena configuraciones clave de la aplicación, como los parámetros de conexión al servidor de prueba, opciones de frecuencia de prueba y cualquier otro valor configurable.
Facilita el ajuste de variables de control para experimentos.

- data_storage.py: Administra el almacenamiento de los datos de las pruebas, utilizando bases de datos SQLite o archivos locales.
Asegura que los resultados sean recuperables para visualización posterior o análisis comparativo.

- device_info.py: Detecta y obtiene información sobre el dispositivo en el cual se realiza la prueba (tipo de hardware, tipo de conexión, etc.).
Permite registrar esta información junto con las métricas de QoS y QoE para análisis detallado.

- utils.py: Contiene funciones auxiliares y comunes (p. ej., cálculo de promedios, validación de URLs, manejo de errores).
Proporciona código reutilizable para mantener otros módulos más organizados y centrados en su funcionalidad principal.
