import math
import numpy

#------------- VARIABLES GLOBALES-------------
tolerancia = 10**(-8)
iteracionesMaximas = 2500
pi = 3.14159265358979323846
#---------------------------------------------

def factorial(x):
    if x==0 or x==1:
        return 1
    else:
        return x * factorial(x-1)

def div_t(x):
    return x**-1

def sin_t(x):
    pass

def tan_t(x):
    pass

def log_t(x, y):
    pass

def sinh_t(x):
    pass

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
    resultado = 0

    for i in range(iteracionesMaximas):
        sk = (x**i) * div_t(factorial(i))
        sk_mas_uno = sk + (x**(i+1)) * div_t(factorial(i+1))

        if abs(sk_mas_uno - sk) < tolerancia:
            break

        resultado += sk

    return resultado

def cos_t(x):
    pass

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