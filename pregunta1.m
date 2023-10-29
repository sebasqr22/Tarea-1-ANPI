%Función que llama al método iterativo HSS para aproximar la solución del sistema de ecuaciones Ax = b.
%No recibe parámetros.
%Retorna el el llamado a la función HSS.
function preunta1()
  clc;

  % Se definen las matrices de ejemplo:
  %Matriz W
  W = [12, -2, 6, -2;
  -2, 5, 2, 1;
  6, 2, 9, -2;
  -2, 1, -2, 1];

  %Matriz T
  T = [6, 2, 7, 2;
  2, 7, 1, 1;
  7, 1, 9, 0;
  2, 1, 0, 10];

  %Matriz p
  p = [9; -7; -5; 7];

  %Matriz q
  q = [12; -4; 17; -2];

  %Número de iteraciones máximas
  iterMax = 1000;

  %Criterio de parada
  tol = 10^(-12);

  %Número de iteraciones máximas
  max_iter = 1000;

  %Llamada a la función que aproxima la solución a través del método HSS
  display("Método HSS:")
  [x, k, error] = HSS(iterMax, W, T, p, q, tol)
endfunction

%Función que implementa computacionalmente el método iterativo HSS para aproximar la solución del sistema de ecuaciones Ax = b.
%Recibe como parámetros a iterMax, W, T, p, q, tol.
  %iterMax es el número máximo de iteraciones a realizar.
  %W es la matriz W del ejemplo.
  %T es la matriz T del ejemplo.
  %p es la matriz p del ejemplo.
  %q es la matriz q del ejemplo.
  %tol es el criterio de parada.
%Retorna el valor aproxima la solución del problema, el número de iteraciones realizados y el porcentaje de error.
  %x es la solución que aproxima el problema.
  %k es el número de iteraciones realizadas.
  %error es el porcentaje de error alcanzado.
function [x, k, error] = HSS(iterMax, W, T, p, q, tol)

  %Obtiene el número filas de W
  m = size(W, 1);

  %Definición de i según el enunciado de la tarea
  i = sqrt(-1);

  %Cálculo de la matriz A
  A = W + i * T;

  %Cálculo de la matriz B
  b = p + i * q;

  %Cálculo de la matriz identidad de tamaño m
  Im = eye(m);

  %Definición del vector inicial.
  xk = zeros(m, 1);

  %Cálculo de la Inversa de(Im+W)
  Inversa1 = mldivide((Im + W), Im);

  %Calculo de (Im - i * T)
  B = Im - i * T;

  %Cálculo de la Inversa de (Im + i * T)
  Inversa2 = mldivide((Im + i * T), Im);

  %Cálculo (Im - W)
  C = Im - W;

  %Cálculo del método iterativo para aproximar la solución del sistema de ecuaciones
  %con el método HSS
  for k = 0:iterMax
    z = Inversa1 * B * xk + Inversa1 * b;
    x = Inversa2 * C * z + Inversa2 * b;
    xk = x;
    %Definición del criterio de parada
    error = norm(A * xk - b);
    %Verificación del criterio de parada
    if error < tol
      break
    endif
   endfor
endfunction
