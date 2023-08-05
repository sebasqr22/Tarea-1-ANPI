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
        resultado = 1
        while x > 1:
            resultado *= x
            x -= 1
        return resultado

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

def sin_t(x): #SIGUE ESTANDO MAL, YA LE PREGUNTE AL PROFE
    parte1 = "(-1)**n"
    parte2 = "a**(2*n+1)"
    parte3 = "div_t(factorial(2*n+1))"
    funcion = expresion(f"{parte1} * ({parte2} * {parte3})")

    return generar_resultado(funcion, x)

def tan_t(x):
    return sin_t(x) * div_t(cos_t(x))

def log_t(x, y):
    pass

def sinh_t(x):
    parte1 = "a**(2*n + 1)"
    parte2 = "div_t(factorial(2*n + 1))"
    funcion = expresion(f"{parte1} * {parte2}")

    return generar_resultado(funcion, x)


def tanh_t(x):
    return sin_t(x) * div_t(cosh_t(x) + 1)

def root_t(x, y):
    return power_t(x, div_t(y))

def atan_t(x):
    parte1 = "(-1)**n"
    antes = "pi * div_t(2)"

    if x >= -1 or x <= 1:
        parte2 = "a**(2*n+1)"
        parte3 = "div_t(2*n+1)"
        funcion = expresion(f"{parte1} * ({parte2} * {parte3})")

        return generar_resultado(funcion, x)

    elif x > 1:
        parte2 = "div_t((2*n+1) * a**(2*n+1))"
        funcion = expresion(f"{antes}-({parte1} * {parte2})")

        return generar_resultado(funcion, x)

    else:
        parte2 = "div_t((2*n+1) * a**(2*n+1))"
        funcion = expresion(f"-{antes}-({parte1} * {parte2})")

        return generar_resultado(funcion, x)
print(atan_t(pi))

def sec_t(x):
    return div_t(cos_t(x))

def csc_t(x):
    return div_t(sin_t(x))

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
    parte1_antes = "2*(a-1)"
    parte2_antes = "div_t(a+1)"

    parte1 = "div_t(2*n+1)"
    parte2 = "a-1"
    parte3 = "div_t(a+1)"
    funcion = expresion(f"({parte1_antes} * {parte2_antes}) * (({parte1}) * ({parte2} * {parte3})**(2*n))")

    return generar_resultado(funcion, x)

def power_t(x,y):
    return x**y

def cosh_t(x):
    parte1 = "a**(2*n)"
    parte2 = "div_t(factorial(2*n))"
    funcion = expresion(f"{parte1} * {parte2}")

    return generar_resultado(funcion, x)

def sqrt_t(x):
    return power_t(x, div_t(2))

def asin_t(x):
    parte1 = "factorial(2*n)"
    parte2 = "div_t(4**n)"
    parte3 = "div_t(factorial(n)**2)"
    parte4 = "div_t(2*n + 1)"
    parte5 = "a**(2*n+1)"
    funcion = expresion(f"({parte1} * {parte2} * {parte3} * {parte4}) * {parte5}")

    return generar_resultado(funcion, x)


def acos_t(x):
    return power_t(cos_t(x), -1)

def cot_t(x):
    return div_t(tan_t(x))
