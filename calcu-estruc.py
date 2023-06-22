import tkinter as tk


def calcular():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operador = entry_operador.get()

        if operador == '+':
            resultado = num1 + num2
        elif operador == '-':
            resultado = num1 - num2
        elif operador == '*':
            resultado = num1 * num2
        elif operador == '/':
            resultado = num1 / num2
        else:
            resultado = "Operador no válido"

        label_resultado.config(text="Resultado: {}".format(resultado))
    except ValueError:
        label_resultado.config(text="Error: Entrada inválida")


# Crear la ventana principal
window = tk.Tk()
window.title("Calculadora")

# Crear los widgets
label_num1 = tk.Label(window, text="Número 1:")
label_num1.pack()

entry_num1 = tk.Entry(window)
entry_num1.pack()

label_operador = tk.Label(window, text="Operador:")
label_operador.pack()

entry_operador = tk.Entry(window)
entry_operador.pack()

label_num2 = tk.Label(window, text="Número 2:")
label_num2.pack()

entry_num2 = tk.Entry(window)
entry_num2.pack()

button_calcular = tk.Button(window, text="Calcular", command=calcular)
button_calcular.pack()

label_resultado = tk.Label(window, text="Resultado:")
label_resultado.pack()

# Ejecutar la aplicación
window.mainloop()