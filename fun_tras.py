import math
import decimal

decimal.getcontext().prec = 100
# 
# Recibe
# Retorna

#------------- VARIABLES GLOBALES-------------
tolerancia = 10**(-8)
iteracionesMaximas = 2500
pi = 3.14159265358979323846
eps = 2.2204 * (10**(-16))
#---------------------------------------------

# Funcion que calcula la potencia de un numero
# Recibe un numero a calcular la potencia y una potencia
# Retorna el resultado de la potencia
def power_t(x,y):
    return x**y

#------------- FUNCIONES GLOBALES-------------

# Funcion que calcula el factorial de un numero
# Recibe un numero a calcular el factorial
# Retorna el resultado de la operacion factorial
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

# Funcion que convierte un string a una funcion matematica
# Recibe un string
# Retorna la funcion matematica lambda segun lo dado con el string
def expresion(expre):
    funcion = eval("lambda n, a:" + expre)
    return funcion

# Funcion que calcula el resultado de la tolerancia
# Recibe el valor de una iteracion junto al valor de la iteracion siguiente
# Retorna un valor de verdad que indica si se paran los ciclos de iteracion
def medir_tolerancia(sk, mas_uno):
    return abs(mas_uno - sk) < tolerancia

# Funcion que genera los resultados de una sumatoria dada
# Recibe la expresion matematica a utilizar y el valor numerico que se utilizara en la operacion
# Retorna el resultado final de la sumatoria
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

# Funcion que calcula el valor inicial de la sucesion utilizada para calcular el inverso de un numero
# Recibe el valor del numero al que se desea obtener el inverso
# Retorna el valor inicial de x0 para la sucesion del inverso de un numero
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

# Funcion que calcula el inverso de un numero, para poder expresar fracciones
# Recibe el valor del numero al que se desea obtener el inverso
# Retorna el resultado de la operacion inverso (^-1)
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

# Funcion que calcula el valor de un seno
# Recibe el valor numero a calcular el seno
# Retorna el resultado de la sumatoria que modela el valor de un seno
def sin_t(x):
    parte1 = "power_t(-1, n)"
    parte2 = "power_t(a, 2*n +1)"
    parte3 = "factorial((2*n)+1)"
    funcion = expresion(f"({parte1}) * ({parte2} * div_t({parte3}))")

    return generar_resultado(funcion, x)


# Funcion que calcula el valor de un logaritmo
# Recibe el numero a calcular el logaritmo y el valor del logaritmo a calcular
# Retorna el resultado de la operacion logaritmo
def log_t(x, y):
    if x>0:
        return ln_t(x) * div_t(ln_t(y))
    else:
        return "ERROR"

# Funcion que calcula el seno hiperbolico de un numero
# Recibe el valor del numero a calcular el seno hiperbolico
# Retorna el resultado de la operacion seno hiperbolico
def sinh_t(x): 
    parte1 = "power_t(a, 2*n +1)"
    parte2 = "div_t(factorial(2*n + 1))"
    funcion = expresion(f"{parte1} * {parte2}")

    return generar_resultado(funcion, x)

# Funcion que calcula la tangente hiperbolica de un numero
# Recibe el numero al que se desea calcular la tangente hiperbolico
# Retorna el resultado de la operacion tangente hiperbolica
def tanh_t(x):
    return sin_t(x) * div_t(cosh_t(x) + 1)

# Funcion que calcula la raiz de un numero
# Recibe el numero de la raiz a calcular y el valor de la raiz a utilizar
# Retorna el resultado de la raiz 
def root_t(x, y):
    if x > 0 and y > 2 and y % 2 == 0:
        xk = x * div_t(2)
        xk_mas_uno = 0

        for n in range(iteracionesMaximas):
            xk_mas_uno = xk - ((power_t(xk, y)-x) * (y * power_t(xk, y-1)))

            if abs(xk_mas_uno-xk) < tolerancia * abs(xk_mas_uno):
                break

            xk = xk_mas_uno

        return xk
    
    elif x > 0:
        return power_t(x, div_t(y))

    else:
        return 1

# Funcion que calcula el arco tangente de un numero
# Recibe el numero a calcular la arco tangente
# Retorna el resultado del calculo de la arco tangente
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
        return -(pi * div_t(2)) - suma

# Funcion que calcula la secante de un numero
# Recibe el numero a calcular la secante
# Retorna el valor de la secante del numero
def sec_t(x):
    if x >= -1 and x <= 1:
        #return div_t(cos_t(x))
        return div_t(cos_t(x))
    else:
        return "ERROR"

# Funcion que calcula la cosecante de un numero
# Recibe el numero a calcular la cosecante
# Retorna el valor de la cosecante del numero dado
def csc_t(x):
    if x >= -1 and x <= 1:
        return div_t(sin_t(x))
    else:
        return "ERROR"

# Funcion que calcula el valor de e elevado a un numero
# Recibe el numero a utilizar como exponente
# Retorna el valor de la e elevada
def exp_t(x):
    funcion = expresion("power_t(a,n) * div_t(factorial(n))")

    return generar_resultado(funcion, x)

# Funcion que calcula el coseno de un numero
# Recibe el numero a calcular el coseno
# Retorna el valor del coseno del numero
def cos_t(x):
    parte1 = "power_t(-1, n)"
    parte2 = "power_t(a, 2*n)"
    parte3 = "div_t(factorial(2*n))"
    funcion = expresion(f"({parte1}) * ( ({parte2}) * ({parte3}) )")

    return generar_resultado(funcion, x)

# Funcion que calcula el logaritmo natural de un numero
# Recibe el valor del numero a calcular el logaritmo natural
# Retorna el valor del logaritmo natural
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
        return ((2*(x-1)) * (div_t(x+1))) * suma
    else:
        return "ERROR"

# Funcion que calcula el coseno hiperbolico de un numero
# Recibe numero a calcularle el coseno hiperbolico
# Retorna el valor del coseno hiperbolico del numero dado
def cosh_t(x):
    parte1 = "power_t(a, 2*n)"
    parte2 = "div_t(factorial(2*n))"
    funcion = expresion(f"{parte1} * {parte2}")

    return generar_resultado(funcion, x)


# Funcion que calcula la raiz cuadrada
# Recibe numero a calcularle la raiz cuadrada
# Retorna la raiz cuadrada del numero recibido
def sqrt_t(x):
    if (x >= 0):
        return power_t(x, div_t(2))
    else:
        return "ERROR"


# Funcion que calcula el arcoseno
# Recibe numero a calcularle el arcoseno
# Retorna el arcoseno del numero recibido
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

# Funcion que calcula el arcocoseno
# Recibe numero a calcularle el arcocoseno
# Retorna el arcocoseno del numero recibido
def acos_t(x):
    if -1 <= x <= 1:
        return pi * div_t(2) - asin_t(x)
    else:
        return "ERROR"

# Funcion que calcula la tangente
# Recibe numero a calcularle la tangente
# Retorna la tangente del numero recibido
def tan_t(x):
    return sin_t(x) * div_t(cos_t(x))

# Funcion que calcula la cotangente
# Recibe numero a calcularle la cotangente
# Retorna la cotangente del numero recibido
def cot_t(x):
    if (abs(sin_t(x)) > (10 ** (-10))):
        return div_t(tan_t(x))
    else:
        return "ERROR"
