from funtras import *

dentro_raiz = cos_t(3 * div_t(7)) + ln_t(2)
raiz = root_t(dentro_raiz, 3)

primera_parte = raiz * div_t(sinh_t(sqrt_t(2)))
segunda_parte = atan_t(exp_t(-1))

op = primera_parte + segunda_parte
print(f"El resultado de la operación es {op}")