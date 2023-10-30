%Función que llama al método iterativo MHSS para el ejemplo específico planteado en el enunciado de la tarea.
%no recibe parámetros.
%Retorna el llamado a la funcion MHSS.
function pregunta3
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

  %Llamada a la función que aproxima la solución a través del método MHSS
  display("Método MHSS:")
  [xk, error, iteraciones, alpha] = mhss(iterMax, W, T, p, q, tol)
endfunction

%Función que implementa computacionalmente el método iterativo MHSS para aproximar la solución del sistema de ecuaciones Ax = b, planteado en el enunciado de la tarea.
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
  %alpha es el valor óptimo de α.
function [xk, error, iteraciones, alpha] = mhss(iterMax, W, T, p, q, tol)

  %Valor imaginario
  i = sqrt(-1);

  %Tamaño de la matriz identidad
  filas = size(W, 1);

  %Matriz identidad de tamaño
  Im = eye(filas);

  %Cálculo de la matriz A
  A = W + i*T;

  %Cálculo de la matriz b
  b = p + i*q;

  %Valor inicial del vector xk
  xk = zeros(size(W,1),1);

  %Calcular los autovalores de W
  Autoval = eig(W);

  %Se calcula el valor propio mínimo
  Autoval_min = min(Autoval);

  %Se calcula el valor propio máximo
  Autoval_max = max(Autoval);

  %Se calcula el valor de α*
  alpha = sqrt(Autoval_min * Autoval_max);

  %Se calcula la inversa de (αIm + T)
  inversaT = mldivide((alpha*Im + T), Im);

  %Se calcula la inversa de (αIm +W)
  inversaW = mldivide((alpha*Im + W), Im);

  %Se calcula M
  M = (inversaT * (alpha*Im + i*W) * inversaW * (alpha*Im - i*T));

  %Se calcula N
  N = ((1 - i) * alpha * inversaT * inversaW);

    for iteraciones=0:iterMax

      %Se calcula el procentaje de error con el nuevo valor de xk
      error = norm(A*xk-b);

      %Se verifica si aun se debe seguir haciendo iteraciones
      if  tol <= error

        %Se establece el nuevo valor de xk
        xk = M*xk + N*b;
      else

        %Se termina con las iteraciones
        break

      end

  endfor


endfunction
