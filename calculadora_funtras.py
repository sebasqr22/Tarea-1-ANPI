from tkinter import *
import tkinter as tk
from fun_tras import *

# Definición del valor pi
pi_t = 3.14159265358979323846

# Se debe instalar pip install numpy imageio
# Se debe inntalar numpy

# Función que registra al Entry como activo cuando se hace clic en él
# Recibe como parámetro Entry, que es el Entry sobre el cual se está hacierdo click
# Retorna poner el estado del Entry como activo
def set_active_entry(entry):
    global active_entry
    active_entry = entry

# Función que se llama cuando se hace clic en un botón numérico u operación
# Recibe como parámetro el contenido del botón en el que se está haciendo click
# Retorna escribir el contenido del bóton en el Entry que esta activo
def write_to_active_entry(num):
    if active_entry:
        current_text = active_entry.get() # Obtiene el contenido actual del Entry activo
        active_entry.delete(0, tk.END) # Borra el contenido actual del Entry
        active_entry.insert(0, current_text + str(num)) # Agrega el número al contenido del Entry

# Función para borrar el contenido de los campos de entrada al presionar el botón "Clear All"
# No recibe parámetros.
# Retorna el visualizar los campos de entrada vacíos
def clear_entries():
    Entradax.delete(0, tk.END)  # Borra el contenido del Entry Entradax
    Entraday.delete(0, tk.END)  # Borra el contenido del Entry Entraday

def cerrar_ventana(ventana_a_cerrar):
    ventana_a_cerrar.destroy()

def help():

    # Se crea la ventana con ayuda de Tkinter, la cual será la calculadora.
    ventana_secundaria = Tk()
    # Se le pone un título vacío a la ventana.
    ventana_secundaria.title("")
    # Se le dan dimensiones a la calculadora.
    ventana_secundaria.geometry("800x800")
    # Se le drinda un color a la calculadora.
    ventana_secundaria.configure(background="Medium Purple")
    #Información de bienvenida e instrucciones sobre el uso de la calculadora.
    Bienvenida = Label(ventana_secundaria, font=('arial', 20, 'bold'), text="Bienvenid@ a Basic Calculator!", bd=5, bg="Medium Purple", justify="center")
    Bienvenida.place(x=185, y=5)

    Info = Label(ventana_secundaria, font=('arial', 15, 'bold'), text="Instrucciones para el uso de la calculadora: ", bd=5, bg="Medium Purple", justify="center")
    Info.place(x=185, y=50)

    instrucciones = "Para utilizar la calculadora, se debe insertar un valor numérico real en el espacio \n " "libre para x. Luego de esto, se debe seleccionar la operación que desea realizar. \n" \
                    "Es importante que se realice una operación a la vez y que cuando esta finalice \n" "verificar que se muestre el resultado en el espacio de Answer. Finalmente,\n" \
                    "se debe utilizar el botón de Clear All para poder continuar con \n" "el uso de la calculadora. \n" "\n A su vez, si en alguna de las operaciones se necesita el valor de y, es\n" \
                    "fundamental que se inserte tanto el valor de x como de y en sus respectivos\n" "espacios antes de realizar la operación que necesite de ambos parámetros. \n" \
                    "\n Por último, validar que la información suministrada tiene sentido matemático, es \n" "decir, que no se indefine o de lo contrario saldra un mensaje de alerta."
    Instrucciones = Label(ventana_secundaria, font=('arial', 15, 'bold'), text= instrucciones, bd=5, bg="Medium Purple", justify="center")
    Instrucciones.place(x=10,y=100)

    Alumnos = Label(ventana_secundaria, font=('arial', 12, 'bold'), text="Alumnos que participaron en el desarrollo de esta tarea:", bd=5, bg="Medium Purple", justify="center")
    Alumnos.place(x=178, y=450)

    alumnos = Label(ventana_secundaria, font=('arial', 12, 'bold'), text="Luis Diego Araya Porras\n" \
                    "\nAndrés Molina Redondo\n" "\nSebastián Quesada\n" "\nSergio Ríos", bd=5, bg="Medium Purple", justify="center")
    alumnos.place(x=300, y=500)

    Button(ventana_secundaria, text="SALIR", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: cerrar_ventana(ventana_secundaria)).place(x=360, y=675)


# Se crea la ventana con ayuda de Tkinter, la cual será la calculadora.
ventana = Tk()
# Se le pone un título vacío a la ventana.
ventana.title("")
# Se le dan dimensiones a la calculadora.
ventana.geometry("650x800")
# Se le drinda un color a la calculadora.
ventana.configure(background="RoyalBlue1")
# Se le asigna un color a la los botones que se crearan en un futuro.
color_boton = ("gray77")

# Se le fijan dimensiones a los botones.
ancho_boton = 10
alto_boton = 3

# Se crea la variable operador vacía.
operador = ""

# Variable que contiene el texto en String insertado en el espacio de "x".
input_textx = StringVar()

# Variable que convierte el texto en int insertado en el espacio de "x".
x = int (input_textx)

# Variable que contiene el texto en String insertado en el espacio de "y".
input_texty = StringVar()

# Se le pone un título a la calculadora y se ubica en la ventana.
Titulo = Label(ventana, font=('arial', 25, 'bold'), text="Basic Calculator", bd=5, bg="RoyalBlue1", justify="center")
Titulo.place(x=200, y=5)

# Se crea un label que contiene la letra "x" y se ubica en la ventana.
Nx = Label(ventana, font=('arial', 15, 'bold'), text="x =", bd=5, bg="RoyalBlue1", justify="center")
Nx.place(x=10, y=90)

# Se crea una entrada para que el usuario inserte el número deseado.
Entradax = Entry(ventana, font=('arial', 20, 'bold'), width=30, textvariable=input_textx, bd=20, insertwidth=4, bg="white", justify="left")
Entradax.place(x=55, y=70)

# Se crea un label que contiene la letra "y" y se ubica en la ventana.
Ny = Label(ventana, font=('arial', 15, 'bold'), text="y =", bd=5, bg="RoyalBlue1", justify="center")
Ny.place(x=10, y=180)

# Se crea una entrada para que el usuario inserte el número deseado.
Entraday = Entry(ventana, font=('arial', 20, 'bold'), width=30, textvariable=input_texty, bd=20, insertwidth=4, bg="white", justify="left")
Entraday.place(x=55, y=160)

# Se crea una laber el cual indica donde se mostrará la respuesta.
Answer = Label(ventana, font=('arial', 15, 'bold'), text="Answer =", bd=5, bg="RoyalBlue1", justify="center")
Answer.place(x=10, y=270)

# Se crea una entrada el cual contendra la respuesta.
Salida = Entry(ventana, font=('arial', 20, 'bold'), width=26, textvariable="", bd=20, insertwidth=4, bg="white", justify="left", state="disabled")
Salida.place(x=115, y=250)

# Se crean los botones y se añaden a la ventana de la calculadora

Button(ventana,text="HELP",bg=color_boton,width=ancho_boton,height=alto_boton,command=help).place(x=10, y=5)

Button(ventana,text="Clear All",bg=color_boton,width=ancho_boton,height=alto_boton,command=clear_entries).place(x=565, y=130)

Button(ventana, text="senh(x)", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: write_to_active_entry("senh(")).place(x=17,y=335)

Button(ventana, text="cosh(x)", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: write_to_active_entry("cosh(")).place(x=107, y=335)

Button(ventana, text="tanh(x)", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: write_to_active_entry("tanh(")).place(x=197, y=335)

Button(ventana, text="asen(x)", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: write_to_active_entry("asen(")).place(x=287, y=335)

Button(ventana, text="acos(x)", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: write_to_active_entry("acos(")).place(x=377, y=335)

Button(ventana, text="atan(x)", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: write_to_active_entry("atan(")).place(x=467, y=335)

Button(ventana, text="sec(x)", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: write_to_active_entry("sec(")).place(x=557, y=335)

Button(ventana, text="csc(x)", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: write_to_active_entry("csc(")).place(x=17, y=400)

Button(ventana, text="cot(x)", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: write_to_active_entry("cot(")).place(x=107, y=400)

Button(ventana, text="sen(x)", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: [sin_t(x)]).place(x=197, y=400)

Button(ventana, text="cos(x)", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: write_to_active_entry("cos(")).place(x=287, y=400)

Button(ventana, text="tan(x)", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: write_to_active_entry("tan(")).place(x=377, y=400)

Button(ventana, text="ln(x)", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: write_to_active_entry("log(")).place(x=467, y=400)

Button(ventana, text="log10(x)", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: write_to_active_entry("log10(")).place(x=557, y=400)

Button(ventana, text="logy(x)", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: write_to_active_entry("logy(")).place(x=17, y=465)

Button(ventana, text="1/x", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: write_to_active_entry("1/")).place(x=107, y=465)

Button(ventana, text="√x", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: write_to_active_entry("sqrt(")).place(x=197, y=465)

Button(ventana, text="y√x", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: write_to_active_entry("ysqrt(")).place(x=287, y=465)

Button(ventana, text="exp(x)", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: write_to_active_entry("**")).place(x=377, y=465)

Button(ventana, text="x^y", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: write_to_active_entry("^")).place(x=467, y=465)

Button(ventana, text="x!", bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: write_to_active_entry("!")).place(x=557, y=465)

Button(ventana,text="7",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:write_to_active_entry(7)).place(x=197,y=530)

Button(ventana,text="8",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:write_to_active_entry(8)).place(x=287,y=530)

Button(ventana,text="9",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:write_to_active_entry(9)).place(x=377,y=530)

Button(ventana,text="4",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:write_to_active_entry(4)).place(x=197,y=595)

Button(ventana,text="5",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:write_to_active_entry(5)).place(x=287,y=595)

Button(ventana,text="6",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:write_to_active_entry(6)).place(x=377,y=595)

Button(ventana,text="1",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:write_to_active_entry(1)).place(x=197,y=660)

Button(ventana,text="2",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:write_to_active_entry(2)).place(x=287,y=660)

Button(ventana,text="3",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:write_to_active_entry(3)).place(x=377,y=660)

Button(ventana,text="0",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:write_to_active_entry(0)).place(x=287,y=725)

Button(ventana,text="π",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:write_to_active_entry(pi_t)).place(x=197,y=725)

Button(ventana,text=".",bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:write_to_active_entry(".")).place(x=377,y=725)

# Registrar los Entry como activos cuando se hace clic en ellos
Entradax.bind("<Button-1>", lambda event: set_active_entry(Entradax))
Entraday.bind("<Button-1>", lambda event: set_active_entry(Entraday))

# Variable global que almacena al Entry activo actualmente
active_entry = None

ventana.mainloop()