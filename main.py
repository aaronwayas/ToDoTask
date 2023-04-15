import tkinter as tk
from tkinter import messagebox

# Función para agregar una tarea a la lista
def agregar_tarea():
    tarea = entrada_tarea.get()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Por favor ingrese una tarea válida.")

# Función para eliminar una tarea de la lista
def eliminar_tarea():
    seleccion = lista_tareas.curselection()
    if seleccion:
        lista_tareas.delete(seleccion)
    else:
        messagebox.showerror("Error", "Por favor seleccione una tarea.")

# Función para marcar una tarea como completada
def completar_tarea():
    seleccion = lista_tareas.curselection()
    if seleccion:
        lista_tareas.itemconfig(seleccion, foreground="gray", selectforeground="gray")
    else:
        messagebox.showerror("Error", "Por favor seleccione una tarea.")

# Función para mostrar una ventana de ayuda
def mostrar_ayuda():
    messagebox.showinfo("Ayuda", "Bienvenido a ToDoTask!\n\n"
                    "Para agregar una tarea, escriba la tarea en el cuadro de texto y haga clic en 'Agregar Tarea'.\n\n"
                    "Para eliminar una tarea, seleccione la tarea en la lista y haga clic en 'Eliminar Tarea'.\n\n"
                    "Para marcar una tarea como completada, seleccione la tarea en la lista y haga clic en 'Completar Tarea'.\n\n"
                    "Disfrute de su lista de tareas!")

# Crear la ventana
ventana = tk.Tk()
ventana.title("ToDoTask - Lista de Tareas")
ventana.geometry("400x300")

# Crear una lista de tareas
lista_tareas = tk.Listbox(ventana, font=("Helvetica", 12), selectmode=tk.SINGLE)
lista_tareas.pack(pady=10, padx=10, expand=True, fill=tk.BOTH)

# Crear una barra de desplazamiento para la lista de tareas
scrollbar = tk.Scrollbar(lista_tareas)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
lista_tareas.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lista_tareas.yview)

# Crear una entrada de texto para agregar tareas
entrada_tarea = tk.Entry(ventana, font=("Helvetica", 12))
entrada_tarea.pack(pady=5, padx=10, expand=True, fill=tk.X)

# Crear un marco para los botones
marco_botones = tk.Frame(ventana)
marco_botones.pack(pady=5)

# Crear botones para agregar, eliminar, completar tareas y mostrar ayuda
btn_agregar = tk.Button(marco_botones, text="Agregar Tarea", command=agregar_tarea)
btn_agregar.pack(side=tk.LEFT, padx=5)
btn_eliminar = tk.Button(marco_botones, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.pack(side=tk.LEFT, padx=5)
btn_completar = tk.Button(marco_botones, text="Completar Tarea", command=completar_tarea)
btn_completar.pack(side=tk.LEFT, padx=5)
btn_ayuda = tk.Button(marco_botones, text="Ayuda", command=mostrar_ayuda)
btn_ayuda.pack(side=tk.LEFT, padx=5)

# Función para cerrar la aplicación
def cerrar_aplicacion():
    ventana.destroy()

# Crear un botón para cerrar la aplicación
btn_cerrar = tk.Button(ventana, text="Cerrar", command=cerrar_aplicacion)
btn_cerrar.pack(pady=10)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
