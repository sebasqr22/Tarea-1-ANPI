import math
from error_window import *
import decimal

decimal.getcontext().prec = 100
#import numpy

#------------- VARIABLES GLOBALES-------------
tolerancia = 10**(-8)
iteracionesMaximas = 2500
pi = 3.14159265358979323846
eps = 2.2204 * (10**(-16))
#---------------------------------------------

def power_t(x,y):
    return x**y

#------------- FUNCIONES GLOBALES-------------
def factorial(x):
    if x==0 or x==1:
        return 1
    elif (x>1):
        resultado = 1
        while x > 1:
            resultado *= x
            x -= 1
        return resultado
    else:
        return  "ERROR"

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

def generar_result_2(a):
    pass
#---------------------------------------------
def det_x0(a):
    valor = 0
    if a > factorial(80) and a < factorial(100):
        return power_t(eps, 15)

    elif a > factorial(60) and a <= factorial(80):
        return power_t(eps, 11)

    elif a > factorial(40) and a <= factorial(60):
        return power_t(eps, 8)

    elif a > factorial(20) and a <= factorial(40):
        return power_t(eps, 4)

    else:
        return power_t(eps, 2)

def div_t(x):
    neg = False
    if x < 0:
        neg = True


    if x >= factorial(100):
        return 0
    elif x == 0:
        return "ERROR"
    else:
        x = abs(x)
        xk = det_x0(x)
        xk_mas_uno = 0
        valor = 0

        for n in range(iteracionesMaximas):
            xk_mas_uno = xk * (2-x*xk)

            if abs(xk_mas_uno-xk) < tolerancia * abs(xk_mas_uno):
                break

            xk = xk_mas_uno
        if(neg):
            xk = -xk
        return xk

def sin_t(x):
    parte1 = "power_t(-1, n)"
    parte2 = "power_t(a, 2*n +1)"
    parte3 = "factorial((2*n)+1)"
    funcion = expresion(f"({parte1}) * ({parte2} * div_t({parte3}))")

    return generar_resultado(funcion, x)

def a_t(x):
    if (abs(cos_t(x)) > 10 ** (-10)):
        return sin_t(x) * div_t(cos_t(x))
    else:
        return "ERROR"


def log_t(x, y):
    if x>0:
        return ln_t(x) * div_t(ln_t(y))
    else:
        return "ERROR"

def sinh_t(x): 
    parte1 = "power_t(a, 2*n +1)"
    parte2 = "div_t(factorial(2*n + 1))"
    funcion = expresion(f"{parte1} * {parte2}")

    return generar_resultado(funcion, x)


def tanh_t(x):
    return sin_t(x) * div_t(cosh_t(x) + 1)

def root_t(x, y):
    if x > 0 and y > 2:
        xk = x * div_t(2)
        xk_mas_uno = 0

        for n in range(iteracionesMaximas):
            xk_mas_uno = xk - ((power_t(xk, y)-x) * (y * power_t(xk, y-1)))

            if abs(xk_mas_uno-xk) < tolerancia * abs(xk_mas_uno):
                break

            xk = xk_mas_uno

        return xk
    else:
        return 1

#print(root_t(4,3))

def atan_t(x): 
    parte1 = "power_t(-1, n)"
    antes = "pi * div_t(2)"

    if x >= -1 and x <= 1:
        suma = 0
        for n in range(iteracionesMaximas):
            n1 = n + 1

            sk = power_t(-1, n) * power_t(x, 2*n+1) * div_t(2*n+1)
            sk1 = power_t(-1, n1) * power_t(x, 2*n1+1) * div_t(2*n1+1)

            if medir_tolerancia(sk, sk1):
                break

            suma += sk
        print(f"SUMAMMMMMMMMMMMMMMMMMMMMAMAAAAAAAAAA {suma}")
        return suma

    elif x > 1:
        suma = 0
        for n in range(iteracionesMaximas): 
            n1 = n + 1

            sk = power_t(-1, n) * (div_t((2*n+1) * power_t(x, 2*n+1)))
            sk1 = power_t(-1, n1) * (div_t((2*n1+1) * power_t(x, 2*n1+1)))

            if medir_tolerancia(sk, sk1):
                break

            suma += sk
        print(f"SUMAMMMMMMMMMMMMMMMMMMMMAMAAAAAAAAAA {suma}")
        return (pi * div_t(2)) - suma

    else:
        suma = 0
        for n in range(iteracionesMaximas):
            n1 = n + 1

            sk = power_t(-1, n) * (div_t((2*n+1) * power_t(x, 2*n+1)))
            sk1 = power_t(-1, n1) * (div_t((2*n1+1) * power_t(x, 2*n1+1)))

            if medir_tolerancia(sk, sk1):
                break

            suma += sk
        print(f"SUMAMMMMMMMMMMMMMMMMMMMMAMAAAAAAAAAA {suma}")
        return (pi * div_t(2)) - suma

def sec_t(x):
    if x >= -1 and x <= 1:
        #return div_t(cos_t(x))
        return div_t(cos_t(x))
    else:
        return "ERROR"

def csc_t(x):
    if x >= -1 and x <= 1:
        return div_t(sin_t(x))
    else:
        return "ERROR"


def exp_t(x):
    funcion = expresion("a**n * div_t(factorial(n))")

    return generar_resultado(funcion, x)

def cos_t(x):
    parte1 = "power_t(-1, n)"
    parte2 = "power_t(a, 2*n)"
    parte3 = "div_t(factorial(2*n))"
    funcion = expresion(f"({parte1}) * ( ({parte2}) * ({parte3}) )")

    return generar_resultado(funcion, x)

def ln_t(x):
    if (x > 0):
        suma = 0
        for n in range(iteracionesMaximas):
            n1 = n + 1

            sk = div_t(2*n+1) * (((x-1) * div_t(x+1))**(2*n))
            sk1 = div_t(2*n1+1) * (((x-1) * div_t(x+1))**(2*n1))

            if medir_tolerancia(sk, sk1):
                break

            suma += sk
        print(f"LNNNNNNNNNNNNNNNNNNNNN {suma}")
        return ((2*(x-1)) * (div_t(x+1))) * suma
    else:
        return "ERROR"


def cosh_t(x):
    parte1 = "power_t(a, 2*n)"
    parte2 = "div_t(factorial(2*n))"
    funcion = expresion(f"{parte1} * {parte2}")

    return generar_resultado(funcion, x)

def sqrt_t(x):
    if (x >= 0):
        return power_t(x, div_t(2))
    else:
        return "ERROR"

def asin_t(x):
    if -1 <= x <= 1: 
        parte1 = "factorial(2*n)"
        parte2 = "div_t(power_t(4,n))"
        parte3 = "div_t(power_t(factorial(n), 2))"
        parte4 = "div_t(2*n + 1)"
        parte5 = "power_t(a, 2*n+1)"
        funcion = expresion(f"({parte1} * {parte2} * {parte3} * {parte4}) * {parte5}")

        return generar_resultado(funcion, x)
    else:
        return "ERROR"

def acos_t(x):
    if -1 <= x <= 1:
        return pi * div_t(2) - asin_t(x)
    else:
        return "ERROR"

def tan_t(x):
    return sin_t(x) * div_t(cos_t(x))

def cot_t(x):
    if (abs(sin_t(x)) > (10 ** (-10))):
        return div_t(tan_t(x))
    else:
        return "ERROR"
