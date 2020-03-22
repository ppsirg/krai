# krai

crontab enhaced with ai

# metas

- se desea ejecutar tareas repetitivas en el momento de menor actividad del sistema (como sincronizaciones, re-inicios)
- se desea tener un registro del uso de los recursos computacionales del servidor

# requisitos

los requisitos para nuestro proyecto de machine learning

- el sistema debe contar con una funcion para monitoreo de recursos
  - la funcion para monitoreo de recursos debe guardar el consumo de cpu, ram y uso de disco del servidor actual linea por linea como un diccionario, asi como el tiempo en el que se tomó la medición
  - la funcion para monitoreo de recursos debe guardar un archivo de log por día
  - la funcion para monitoreo de recursos debe contar con la funcionalidad de configurar el tiempo entre la toma de datos de consumo de cpu, ram y uso de disco
- el sistema debe contar con una funcion para determinar la hora de ejecución de una tarea definida
  - la funcion para determinar la hora de ejecución debe contar con la capacidad de configurar una hora por defecto inicial, la cual se usará mientras el sistema no tenga más datos en los que basarse para determinar dicha hora
  - la funcion para determinar la hora de ejecución debe tener una inteligencia artificial que analice los logs generados por la funcion de monitoreo de recursos y determine los lapsos en los que menos carga de cpu y ram existe
  - la funcion para determinar la hora de ejecución debe agendar la ejecución de tareas en los lapsos determinados como los de menor consumo
- el sistema debe contar con una funcion para ejecutar una tarea agendada
  - la funcion para ejecutar una tarea agendada debe ejecutar dicha tarea como un sub-proceso
  - la funcion para ejecutar una tarea agendada debe registrar del tiempo de inicio y final de la tarea
  - la funcion para ejecutar una tarea agendada debe evitar ejecutar dos tareas al mismo tiempo
