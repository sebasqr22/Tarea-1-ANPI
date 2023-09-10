from tkinter import *
import tkinter as tk
from fun_tras import *
from help_window import *

# Se debe instalar pip install numpy imageio
# Se debe inntalar numpy

# Función que registra al Entry como activo cuando se hace clic en él.
# Recibe como parámetro Entry, que es el Entry sobre el cual se está hacierdo click.
# Retorna poner el estado del Entry como activo.
def set_active_entry(entry):
    global active_entry
    active_entry = entry

# Función que se llama cuando se hace clic en un botón numérico u operación.
# Recibe como parámetro el contenido del botón en el que se está haciendo click.
# Retorna escribir el contenido del bóton en el Entry que esta activo.
def write_to_active_entry(num):
    if active_entry:
        current_text = active_entry.get() # Obtiene el contenido actual del Entry activo
        active_entry.delete(0, tk.END) # Borra el contenido actual del Entry
        active_entry.insert(0, current_text + str(num)) # Agrega el número al contenido del Entry

# Función para borrar el contenido de los campos de entrada al presionar el botón "Clear All".
# No recibe parámetros.
# Retorna el visualizar los campos de entrada vacíos.
def clear_entries():
    Entradax.delete(0, tk.END)  # Borra el contenido del Entry Entradax
    Entraday.delete(0, tk.END)  # Borra el contenido del Entry Entraday
    Salida.delete(0, END) #Borra el contenido del Entry Salida

# Función para cerrar la ventana al presionar el botón de salir.
# Recibe como párametro la ventana a cerrar.
# Realiza el cierre de la ventana.
def cerrar_ventana(ventana_a_cerrar):
    ventana_a_cerrar.destroy()

# Función para cerrar la ventana al presionar el botón de salir.
# Recibe como párametro la ventana a cerrar.
# Realiza el cierre de la ventana.
def colocar_respuesta(respuesta):
    Salida.delete(0, END)
    Salida.insert(0, str(respuesta))
    return 0

# Se crea la ventana con ayuda de Tkinter, la cual será la calculadora.
ventana = Tk()
# Se le pone un título vacío a la ventana.
ventana.title("")
# Se le dan dimensiones a la calculadora.
ventana.geometry("650x800")
# Se le drinda un color a la calculadora.
ventana.configure(background="RoyalBlue1")
# Se deja el tamaño de la ventana fija.
ventana.resizable(False, False)



# Fuente que se utilizara para los botones.
Fuente = ("Georgia", 12)
# Se le fijan dimensiones a los botones.
ancho_boton = 8
alto_boton = 2
# Se le asigna un color a la los botones.
color_boton = ("gray77")

# Variable que contiene el texto en String de la respuesta.
respuesta = StringVar()

# Se le pone un título a la calculadora y se ubica en la ventana.
Titulo = Label(ventana, font=(Fuente, 25, 'bold'), text="Basic Calculator", bd=5, bg="RoyalBlue1", justify="center")
Titulo.place(x=200, y=5)

# Se crea un label que contiene la letra "x" y se ubica en la ventana.
Nx = Label(ventana, font=(Fuente, 15, 'bold'), text="x =", bd=5, bg="RoyalBlue1", justify="center")
Nx.place(x=10, y=90)

# Se crea una entrada para que el usuario inserte el número deseado.
Entradax = Entry(ventana, font=(Fuente, 20, 'bold'), width=30, bd=20, insertwidth=4, bg="white", justify="left")
Entradax.place(x=55, y=70)

# Se crea un label que contiene la letra "y" y se ubica en la ventana.
Ny = Label(ventana, font=(Fuente, 15, 'bold'), text="y =", bd=5, bg="RoyalBlue1", justify="center")
Ny.place(x=10, y=180)

# Se crea una entrada para que el usuario inserte el número deseado.
Entraday = Entry(ventana, font=(Fuente, 20, 'bold'), width=30, bd=20, insertwidth=4, bg="white", justify="left")
Entraday.place(x=55, y=160)

# Se crea una laber el cual indica donde se mostrará la respuesta.
Answer = Label(ventana, font=(Fuente, 15, 'bold'), text="Answer =", bd=5, bg="RoyalBlue1", justify="center")
Answer.place(x=10, y=270)

# Se crea una entrada el cual contendra la respuesta.
Salida = Entry(ventana, font=(Fuente, 20, 'bold'), width=26, bd=20, insertwidth=4, bg="white", justify="left", state="normal")
Salida.place(x=115, y=250)

# Función para llamar a la ventana de ayuda
# No recibe parámetros.
# Realiza el llamado a la función de la ventana de ayuda
def llamar_help():
    help_fun()

# Se crean los botones y se añaden a la ventana de la calculadora
Button(ventana, text="HELP", font=Fuente, bg=color_boton, width=ancho_boton, height=alto_boton, command=llamar_help).place(x=10, y=5)

Button(ventana,text="Clear All", font=Fuente, bg=color_boton,width=ancho_boton,height=alto_boton,command=clear_entries).place(x=565, y=130)

Button(ventana, text="senh(x)", font=Fuente, bg=color_boton, width=ancho_boton, height=alto_boton, command = lambda: colocar_respuesta(sinh_t(float(Entradax.get()))) ).place(x=17,y=335)

Button(ventana, text="cosh(x)", font=Fuente, bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: colocar_respuesta(cosh_t(float(Entradax.get()))) ).place(x=107, y=335)

Button(ventana, text="tanh(x)", font=Fuente, bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: colocar_respuesta(tanh_t(float(Entradax.get()))) ).place(x=197, y=335)

Button(ventana, text="asen(x)", font=Fuente, bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: colocar_respuesta(asin_t(float(Entradax.get()))) ).place(x=287, y=335)

Button(ventana, text="acos(x)", font=Fuente, bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: colocar_respuesta(acos_t(float(Entradax.get()))) ).place(x=377, y=335)

Button(ventana, text="atan(x)", font=Fuente, bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: colocar_respuesta(atan_t(float(Entradax.get()))) ).place(x=467, y=335)

Button(ventana, text="sec(x)", font=Fuente, bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: colocar_respuesta(sec_t(float(Entradax.get()))) ).place(x=557, y=335)

Button(ventana, text="csc(x)", font=Fuente, bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: colocar_respuesta(csc_t(float(Entradax.get()))) ).place(x=17, y=400)

Button(ventana, text="cot(x)", font=Fuente, bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: colocar_respuesta(cot_t(float(Entradax.get()))) ).place(x=107, y=400)

Button(ventana, text="sen(x)", font=Fuente, bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: colocar_respuesta(sin_t(float(Entradax.get()))) ).place(x=197, y=400)

Button(ventana, text="cos(x)", font=Fuente, bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: colocar_respuesta(cos_t(float(Entradax.get()))) ).place(x=287, y=400)

Button(ventana, text="tan(x)", font=Fuente, bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: colocar_respuesta(tan_t(float(Entradax.get()))) ).place(x=377, y=400)

Button(ventana, text="ln(x)", font=Fuente, bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: colocar_respuesta(ln_t(float(Entradax.get()))) ).place(x=467, y=400)

Button(ventana, text="logy(x)", font=Fuente, bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: colocar_respuesta(log_t(float(Entradax.get()), float(Entraday.get()))) ).place(x=557, y=400)

Button(ventana, text="1/x", font=Fuente, bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: colocar_respuesta(div_t(float(Entradax.get()))) ).place(x=65, y=465)

Button(ventana, text="√x", font=Fuente, bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: colocar_respuesta(sqrt_t(float(Entradax.get()))) ).place(x=155, y=465)

Button(ventana, text="y√x", font=Fuente, bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: colocar_respuesta(root_t(float(Entradax.get()), float(Entraday.get()))) ).place(x=245, y=465)

Button(ventana, text="exp(x)", font=Fuente, bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: colocar_respuesta(exp_t(float(Entradax.get()))) ).place(x=335, y=465)

Button(ventana, text="x^y", font=Fuente, bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: colocar_respuesta(power_t(float(Entradax.get()), float(Entraday.get()))) ).place(x=425, y=465)

Button(ventana, text="x!", font=Fuente, bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: colocar_respuesta(factorial(float(Entradax.get()))) ).place(x=515, y=465)

Button(ventana,text="7", font=Fuente, bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:write_to_active_entry(7)).place(x=197,y=530)

Button(ventana,text="8", font=Fuente, bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:write_to_active_entry(8)).place(x=287,y=530)

Button(ventana,text="9", font=Fuente, bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:write_to_active_entry(9)).place(x=377,y=530)

Button(ventana,text="4", font=Fuente, bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:write_to_active_entry(4)).place(x=197,y=595)

Button(ventana,text="5", font=Fuente, bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:write_to_active_entry(5)).place(x=287,y=595)

Button(ventana,text="6", font=Fuente, bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:write_to_active_entry(6)).place(x=377,y=595)

Button(ventana,text="1", font=Fuente, bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:write_to_active_entry(1)).place(x=197,y=660)

Button(ventana,text="2", font=Fuente, bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:write_to_active_entry(2)).place(x=287,y=660)

Button(ventana,text="3", font=Fuente, bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:write_to_active_entry(3)).place(x=377,y=660)

Button(ventana,text="0", font=Fuente, bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:write_to_active_entry(0)).place(x=287,y=725)

Button(ventana,text="π", font=Fuente, bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:write_to_active_entry(pi)).place(x=197,y=725)

Button(ventana,text=".", font=Fuente, bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:write_to_active_entry(".")).place(x=377,y=725)

# Registrar los Entry como activos cuando se hace clic en ellos.
Entradax.bind("<Button-1>", lambda event: set_active_entry(Entradax))
Entraday.bind("<Button-1>", lambda event: set_active_entry(Entraday))

# Variable global que almacena al Entry activo actualmente.
active_entry = None

ventana.mainloop()