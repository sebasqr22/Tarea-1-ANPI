from tkinter import *
import tkinter as tk
from tkinter import ttk

# Función para cerrar la ventana al presionar el botón de salir.
# Recibe como párametro la ventana a cerrar.
# Realiza el cierre de la ventana
def cerrar_ventana(ventana_a_cerrar):
    ventana_a_cerrar.destroy()

# Fuente que se utilizara para los botones
Fuente = ("Georgia", 12)
# Se le fijan dimensiones a los botones.
ancho_boton = 5
alto_boton = 2
# Se le asigna un color a la los botones.
color_boton = ("gray77")

def error():
    # Datos de que contiene las funciones y sus dominios para la tabla
    datos_tabla = [
        ["Función", "Dominio"],
        ["senh(x)", "x ∈ R"],
        ["cosh(x)", "x ∈ R"],
        ["tanh(x)", "x ∈ R"],
        ["asen(x)", "x ∈ [-1, 1]"],
        ["acos(x)", "x ∈ [-1, 1]"],
        ["atan(x)", "x ∈ R"],
        ["sec(x)", "x ∈ R \ {π/2 + kπ}, k ∈ Z"],
        ["csc(x)", "x ∈ R \ {kπ}, k ∈ Z"],
        ["cot(x)", "x ∈ R \ {kπ}, k ∈ Z"],
        ["sen(x)", "x ∈ R"],
        ["cos(x)", "x ∈ R"],
        ["tan(x)", "x ∈ R \ {π/2 + kπ}, k ∈ Z"],
        ["ln(x)", "x > 0"],
        ["log10(x)", "x > 0"],
        ["logy(x)", "x > 0"],
        ["1/x", "x ∈ R \ {0}"],
        ["√x", "x ≥ 0"],
        ["y√x", "Si y es par: x ≥ 0 & si y es impar: x ∈ R"],
        ["exp(x)", "x ∈ R"],
        ["x^y", "x ∈ R"],
        ["x!", "x ≥ 0"]
    ]

    # Se crea la ventana con el mensaje relacionado al dominio
    ventana = tk.Tk()
    # Se le dan dimensiones a la ventana.
    ventana.geometry("500x385")
    # Se le pone un título a la ventana.
    ventana.title("Precaución!")
    # Se le drinda un color a la calculadora.
    ventana.configure(background="SpringGreen2")
    # Se deja el tamaño de la ventana fija
    ventana.resizable(False, False)

    #Información relacionada al error.
    Mensaje = Label(ventana, font=('arial', 12, 'bold'), text="Parace que la operación insertada no tiene sentido matemático", bd=5, bg="SpringGreen2", justify="center")
    Mensaje.place(x=5, y=5)

    Mensaje2 = Label(ventana, font=('arial', 10, 'bold'), text="Verifica el dominio de las funciones de la calculadora en la siguiente tabla", bd=5, bg="SpringGreen2", justify="center")
    Mensaje2.place(x=5, y=35)

    # Coordenadas (x, y) para posicionar la tabla en la ventana
    x_pos = 33
    y_pos = 75

    # Crear un Treeview para mostrar la tabla
    tabla = ttk.Treeview(ventana, columns=datos_tabla[0], show="headings")
    for columna in datos_tabla[0]:
        tabla.heading(columna, text=columna)
        tabla.column(columna, width=215)  # Ajustar el ancho de la columna

    # Insertar los datos en la tabla
    for fila in datos_tabla[1:]:
        tabla.insert("", "end", values=fila)

    # Colocar la tabla en las coordenadas especificadas
    tabla.place(x=x_pos, y=y_pos)

    # Botón para cerrar la ventana.
    Button(ventana, text="Cerrar", font=Fuente,  bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: cerrar_ventana(ventana)).place(x=225, y=325)

    # Inicia el bucle principal de la interfaz gráfica de la ventana del error
    ventana.mainloop()