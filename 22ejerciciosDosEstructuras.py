##Ordena la lista de tareas en una cola // entre más pequeño sea el número
##la prioridad es mucho mayor.

tareas = [
    [6, 'Distribucion'],
    [2, 'Diseño'],
    [1, 'Concepcion'],
    [7, 'Mantenimiento'],
    [4, 'Producción'],
    [3, 'Planificación'],
    [5, 'Pruebas']
]

print("Tareas en desorden")
for tarea in tareas:
    print(tarea)

print("Tareas en orden ascendente")
tareas.sort()
for tarea in tareas:
    print(tarea)

print("Tareas en orden descendente")
tareas = tareas[::-1]
for tarea in tareas:
    print(tarea)

