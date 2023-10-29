function [m, k, error] = hss(iterMax, W, T, p, q, tol, m)

  %Obtiene el número filas de W
  filas = size(W, 1);

  %Definición de i según el enunciado de la tarea
  i = sqrt(-1);

  %Cálculo de la matriz A
  A = W + i * T;

  %Cálculo de la matriz B
  b = p + i * q;

  %Cálculo de la matriz identidad de tamaño filas
  Im = eye(filas);

  %Definición del vector inicial.
  xk = zeros(filas, 1);

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
