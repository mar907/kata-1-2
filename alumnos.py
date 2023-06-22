import tkinter as tk
import sqlite3


class AppAlumnos:
    def __init__(self, window):
        self.window = window
        self.window.title("App Alumnos")

        # Conexión a la base de datos
        self.conexion = sqlite3.connect("alumnos.db")
        self.cursor = self.conexion.cursor()

        # Crear la tabla de alumnos si no existe
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS alumnos (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, edad INTEGER)"
        )
        self.conexion.commit()

        # Crear los widgets
        self.button_agregar = tk.Button(self.window, text="Agregar", command=self.abrir_ventana_agregar)
        self.button_agregar.grid(row=0, column=0, padx=5, pady=5)

        self.button_eliminar = tk.Button(self.window, text="Eliminar", command=self.abrir_ventana_eliminar)
        self.button_eliminar.grid(row=0, column=1, padx=5, pady=5)

        self.button_actualizar = tk.Button(self.window, text="Actualizar", command=self.abrir_ventana_actualizar)
        self.button_actualizar.grid(row=0, column=2, padx=5, pady=5)

        self.button_mostrar = tk.Button(self.window, text="Mostrar", command=self.mostrar_alumnos)
        self.button_mostrar.grid(row=0, column=3, padx=5, pady=5)

        self.textarea_alumnos = tk.Text(self.window, height=10, width=40)
        self.textarea_alumnos.grid(row=1, column=0, columnspan=4, padx=5, pady=5)

    def abrir_ventana_agregar(self):
        ventana_agregar = tk.Frame(self.window)
        ventana_agregar.title("Agregar Alumno")

        label_nombre = tk.Label(ventana_agregar, text="Nombre:")
        label_nombre.grid(row=0, column=0, padx=5, pady=5)
        entry_nombre = tk.Entry(ventana_agregar)
        entry_nombre.grid(row=0, column=1, padx=5, pady=5)

        label_edad = tk.Label(ventana_agregar, text="Edad:")
        label_edad.grid(row=1, column=0, padx=5, pady=5)
        entry_edad = tk.Entry(ventana_agregar)
        entry_edad.grid(row=1, column=1, padx=5, pady=5)

        button_guardar = tk.Button(
            ventana_agregar, text="Guardar", command=lambda: self.agregar_alumno(entry_nombre.get(), entry_edad.get())
        )
        button_guardar.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def abrir_ventana_eliminar(self):
        ventana_eliminar = tk.Toplevel(self.window)
        ventana_eliminar.title("Eliminar Alumno")

        label_id = tk.Label(ventana_eliminar, text="ID:")
        label_id.grid(row=0, column=0, padx=5, pady=5)
        entry_id = tk.Entry(ventana_eliminar)
        entry_id.grid(row=0, column=1, padx=5, pady=5)

        button_eliminar = tk.Button(
            ventana_eliminar, text="Eliminar", command=lambda: self.eliminar_alumno(entry_id.get())
        )
        button_eliminar.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    def abrir_ventana_actualizar(self):
        ventana_actualizar = tk.Toplevel(self.window)
        ventana_actualizar.title("Actualizar Alumno")

        label_id = tk.Label(ventana_actualizar, text="ID:")
        label_id.grid(row=0, column=0, padx=5, pady=5)
        entry_id = tk.Entry(ventana_actualizar)
        entry_id.grid(row=0, column=1, padx=5, pady=5)

        label_nombre = tk.Label(ventana_actualizar, text="Nuevo nombre:")
        label_nombre.grid(row=1, column=0, padx=5, pady=5)
        entry_nombre = tk.Entry(ventana_actualizar)
        entry_nombre.grid(row=1, column=1, padx=5, pady=5)

        label_edad = tk.Label(ventana_actualizar, text="Nueva edad:")
        label_edad.grid(row=2, column=0, padx=5, pady=5)
        entry_edad = tk.Entry(ventana_actualizar)
        entry_edad.grid(row=2, column=1, padx=5, pady=5)

        button_actualizar = tk.Button(
            ventana_actualizar,
            text="Actualizar",
            command=lambda: self.actualizar_alumno(entry_id.get(), entry_nombre.get(), entry_edad.get()),
        )
        button_actualizar.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def agregar_alumno(self, nombre, edad):
        self.cursor.execute("INSERT INTO alumnos (nombre, edad) VALUES (?, ?)", (nombre, edad))
        self.conexion.commit()

    def eliminar_alumno(self, alumno_id):
        self.cursor.execute("DELETE FROM alumnos WHERE id = ?", (alumno_id,))
        self.conexion.commit()

    def actualizar_alumno(self, alumno_id, nombre, edad):
        self.cursor.execute("UPDATE alumnos SET nombre = ?, edad = ? WHERE id = ?", (nombre, edad, alumno_id))
        self.conexion.commit()

    def mostrar_alumnos(self):
        self.textarea_alumnos.delete(1.0, tk.END)

        self.cursor.execute("SELECT * FROM alumnos")
        alumnos = self.cursor.fetchall()

        for alumno in alumnos:
            self.textarea_alumnos.insert(tk.END, f"ID: {alumno[0]}\n")
            self.textarea_alumnos.insert(tk.END, f"Nombre: {alumno[1]}\n")
            self.textarea_alumnos.insert(tk.END, f"Edad: {alumno[2]}\n")
            self.textarea_alumnos.insert(tk.END, "============================\n")


# Crear la ventana principal
window = tk.Tk()

# Crear la instancia de la aplicación de alumnos
app_alumnos = AppAlumnos(window)

# Ejecutar la aplicación
window.mainloop()