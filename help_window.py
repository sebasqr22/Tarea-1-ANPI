from tkinter import *
import tkinter as tk

# Función para cerrar la ventana al presionar el botón de salir.
# Recibe como párametro la ventana a cerrar.
# Realiza el cierre de la ventana
def cerrar_ventana(ventana_a_cerrar):
    ventana_a_cerrar.destroy()

# Fuente que se utilizara para los botones
Fuente = ("Georgia", 12)
# Se le fijan dimensiones a los botones.
ancho_boton = 8
alto_boton = 2
# Se le asigna un color a la los botones.
color_boton = ("gray77")

def help_fun():
    # Se crea la ventana con ayuda de Tkinter, la cual será la calculadora.
    ventana_secundaria = Tk()
    # Se le pone un título vacío a la ventana.
    ventana_secundaria.title("")
    # Se le dan dimensiones a la calculadora.
    ventana_secundaria.geometry("800x735")
    # Se le drinda un color a la calculadora.
    ventana_secundaria.configure(background="Medium Purple")
    #Información de bienvenida e instrucciones sobre el uso de la calculadora.
    Bienvenida = Label(ventana_secundaria, font=('arial', 20, 'bold'), text="Bienvenid@ a Basic Calculator!", bd=5, bg="Medium Purple", justify="center")
    Bienvenida.place(x=185, y=5)

    Info = Label(ventana_secundaria, font=('arial', 15, 'bold'), text="Instrucciones para el uso de la calculadora: ", bd=5, bg="Medium Purple", justify="center")
    Info.place(x=185, y=50)

    instrucciones = "Para utilizar la calculadora, se debe insertar un valor numérico real en el espacio \n " "libre para x. Luego de esto, se debe seleccionar la operación que desea realizar. \n" \
                    "Es importante que se realice una operación a la vez y que cuando esta finalice \n" "verificar que se muestre el resultado en el espacio de Answer. Finalmente,\n" \
                    "se debe utilizar el botón de Clear All en caso de que se \n" "requieran limpiar los espacios. \n" "\n A su vez, si en alguna de las operaciones se necesita el valor de y, es\n" \
                    "fundamental que se inserte tanto el valor de x como de y en sus respectivos\n" "espacios antes de realizar la operación que necesite de ambos parámetros. \n" \
                    "\n Por último, validar que la información suministrada tiene sentido matemático, es \n" "decir, que no se indefine o de lo contrario saldrá un mensaje de alerta."
    Instrucciones = Label(ventana_secundaria, font=('arial', 15, 'bold'), text= instrucciones, bd=5, bg="Medium Purple", justify="center")
    Instrucciones.place(x=10,y=100)

    Alumnos = Label(ventana_secundaria, font=('arial', 12, 'bold'), text="Alumnos que participaron en el desarrollo de esta tarea:", bd=5, bg="Medium Purple", justify="center")
    Alumnos.place(x=178, y=450)

    nombres = Label(ventana_secundaria, font=('arial', 12, 'bold'), text="Luis Diego Araya Porras\n" \
                    "\nAndrés Molina Redondo\n" "\nSebastián Quesada\n" "\nSergio Ríos", bd=5, bg="Medium Purple", justify="center")
    nombres.place(x=300, y=500)
    # Botón para cerrar la ventana.
    Button(ventana_secundaria, text="SALIR", font=Fuente,  bg=color_boton, width=ancho_boton, height=alto_boton, command=lambda: cerrar_ventana(ventana_secundaria)).place(x=360, y=675)