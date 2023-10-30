%Funcion que implementa computacionalmente el método iterativo MHSS.
%Recibe las iteraciones maximas, W, T, p, q (que son vectores) y la toleracia
%Retorna el tama˜no de sistema de ecuaciones a resolver, la cantidad de iteraciones y el % de error.
function [m, error, iteraciones] = mhss(iterMax, W, T, p, q, tol, m)

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

