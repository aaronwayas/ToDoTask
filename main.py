class Tarea:
    def __init__(self, nombre, descripcion, fecha_vencimiento):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_vencimiento = fecha_vencimiento
        self.completada = False

# Lista para almacenar las tareas
tareas = []

# Función para agregar una tarea
def agregar_tarea():
    nombre = input("Ingrese el nombre de la tarea: ")
    descripcion = input("Ingrese la descripción de la tarea: ")
    fecha_vencimiento = input("Ingrese la fecha de vencimiento de la tarea: ")
    tarea = Tarea(nombre, descripcion, fecha_vencimiento)
    tareas.append(tarea)
    print("Tarea agregada con éxito!")

# Función para eliminar una tarea
def eliminar_tarea():
    nombre = input("Ingrese el nombre de la tarea a eliminar: ")
    tarea_encontrada = None
    for tarea in tareas:
        if tarea.nombre == nombre:
            tarea_encontrada = tarea
            break
    if tarea_encontrada:
        tareas.remove(tarea_encontrada)
        print("Tarea eliminada con éxito!")
    else:
        print("Tarea no encontrada.")

# Función para marcar una tarea como completada
def marcar_completada():
    nombre = input("Ingrese el nombre de la tarea completada: ")
    for tarea in tareas:
        if tarea.nombre == nombre:
            tarea.completada = True
            print("Tarea marcada como completada.")
            break
    else:
        print("Tarea no encontrada.")

# Bucle principal para la interfaz de línea de comandos
while True:
    print("Bienvenido/a a la lista de tareas!")
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Marcar tarea como completada")
    print("4. Salir")
    opcion = input("Ingrese su opción: ")
    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        eliminar_tarea()
    elif opcion == "3":
        marcar_completada()
    elif opcion == "4":
        print("Gracias por usar la lista de tareas. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")
