import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import pickle

class ToDoTask:
    def __init__(self, text, completed=False):
        self.text = text
        self.completed = completed

class ToDoTaskApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('ToDoTask v0.3')
        self.root.geometry("800x600")  # Tamaño de ventana modificado

        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label='Archivos', menu=self.file_menu)
        self.file_menu.add_command(label='Abrir', command=self.open_tasks)
        self.file_menu.add_command(label='Guardar', command=self.save_tasks)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Salir', command=self.root.quit)

        self.info_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label='Información', menu=self.info_menu)
        self.info_menu.add_command(label='Creador', command=self.show_creator)

        self.task_list = tk.Frame(self.root)
        self.task_list.pack(pady=10)

        self.task_input = tk.Entry(self.root, font=('Helvetica', 16))  # Tamaño de fuente del cuadro de texto modificado
        self.task_input.pack(pady=5, padx=20)  # Añadido padding en x

        self.add_button = tk.Button(self.root, text='Agregar', font=('Helvetica', 14), command=self.add_task)  # Tamaño de fuente del botón modificado
        self.add_button.pack(pady=10)  # Añadido padding en y

        self.tasks = []

    def add_task(self):
        task_text = self.task_input.get().strip()
        if task_text != '':
            task_item = tk.Frame(self.task_list)
            task_item.pack(side=tk.TOP)
            task_checkbox = tk.Checkbutton(task_item, command=lambda: self.toggle_task(task_item))
            task_checkbox.pack(side=tk.LEFT)
            task_label = tk.Label(task_item, text=task_text)
            task_label.pack(side=tk.LEFT)
            self.tasks.append(ToDoTask(text=task_text, completed=False))
            self.task_input.delete(0, tk.END)

    def toggle_task(self, task_item):
        task_index = self.task_list.children.index(task_item)
        self.tasks[task_index].completed = not self.tasks[task_index].completed
        task_item.configure(bg='gray' if self.tasks[task_index].completed else 'white')

    def open_tasks(self):
        file_path = filedialog.askopenfilename(filetypes=[('Archivo de tareas', '*.tdt')])
        if file_path:
            try:
                with open(file_path, 'rb') as file:
                    self.tasks = pickle.load(file)
                    self.refresh_task_list()
            except Exception as e:
                messagebox.showerror('Error', f'Error al abrir el archivo: {e}')

    def save_tasks(self):
        file_path = filedialog.asksaveasfilename(filetypes=[('Archivo de tareas', '*.tdt')],
                                                defaultextension='.tdt')
        if file_path:
            try:
                with open(file_path, 'wb') as file:
                    pickle.dump(self.tasks, file)
                    messagebox.showinfo('Guardado', 'Tareas guardadas correctamente')
            except Exception as e:
                messagebox.showerror('Error', f'Error al guardar el archivo: {e}')

    def show_creator(self):
        messagebox.showinfo('Creador', 'Esta aplicación fue creada por aaronwayas')

    def refresh_task_list(self):
        # Limpiar la lista de tareas actual
        for child in self.task_list.winfo_children():
            child.destroy()

        # Mostrar las tareas en la lista
        for task in self.tasks:
            task_item = tk.Frame(self.task_list)
            task_item.pack(side=tk.TOP)
            task_checkbox = tk.Checkbutton(task_item, command=lambda: self.toggle_task(task_item))
            task_checkbox.pack(side=tk.LEFT)
            task_label = tk.Label(task_item, text=task.text)
            task_label.pack(side=tk.LEFT)
            if task.completed:
                task_item.configure(bg='gray')

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = ToDoTaskApp()
    app.run()


   
