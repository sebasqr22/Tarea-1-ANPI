import math
import numpy

#------------- VARIABLES GLOBALES-------------
tolerancia = 10**(-8)
iteracionesMaximas = 2500
pi = 3.14159265358979323846
#---------------------------------------------

#------------- FUNCIONES GLOBALES-------------
def factorial(x):
    if x==0 or x==1:
        return 1
    else:
        return x * factorial(x-1)

def expresion(expre):
    funcion = eval("lambda n, a:" + expre)
    return funcion


def medir_tolerancia(sk, mas_uno):
    return abs(mas_uno - sk) < tolerancia

def generar_resultado(expresion, a):
    suma = 0
    for n in range(iteracionesMaximas):
        sk = expresion(n, a)
        sk_mas_uno = sk + expresion(n+1, a)

        if medir_tolerancia(sk, sk_mas_uno):
            break

        suma += sk

    return suma
#---------------------------------------------

def div_t(x):
    return x**-1

def sin_t(x): #no se porque pero no me esta sirviendo
    suma = 0
    primera_parte = "(-1)**n"
    segunda_parte = "(a**((2*n) + 1)) * (div_t(factorial((2*n) + 1)))"
    funcion = expresion(f"{primera_parte} * {segunda_parte}")
    for n in range(iteracionesMaximas):
        sk = funcion(n, x)
        sk_mas_uno = sk + funcion(n+1, x)

        if medir_tolerancia(sk, sk_mas_uno):
            break

        suma += sk
    return suma


def tan_t(x):
    pass

def log_t(x, y):
    pass

def sinh_t(x):
    parte1 = "a**(2*n + 1)"
    parte2 = "div_t(factorial(2*n + 1))"
    funcion = expresion(f"{parte1} * {parte2}")

    return generar_resultado(funcion, x)


def tanh_t(x):
    pass

def root_t(x, y):
    pass

def atan_t(x):
    pass

def sec_t(x):
    pass

def csc_t(x):
    pass

def exp_t(x):
    funcion = expresion("a**n * div_t(factorial(n))")

    return generar_resultado(funcion, x)


def cos_t(x): #tampoco sirve
    parte1 = "(-1)**n"
    parte2 = "a**(2*n)"
    parte3 = "div_t(factorial(2**n))"
    funcion = expresion(f"({parte1}) * ( ({parte2}) * ({parte3}) )")

    return generar_resultado(funcion, x)

def ln_t(x):
    pass

def power_t(x,y):
    pass

def cosh_t(x):
    pass

def sqrt_t(x):
    pass

def asin_t(x):
    pass

def acos_t(x):
    pass

def cot_t(x):
    pass