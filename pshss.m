%Función que implementa computacionalmente el método iterativo PSHSS para aproximar la solución del sistema de ecuaciones Ax = b.
%Recibe como parámetros a iterMax, W, T, p, q, tol.
  %iterMax es el número máximo de iteraciones a realizar.
  %W es la matriz W del ejemplo.
  %T es la matriz T del ejemplo.
  %p es la matriz p del ejemplo.
  %q es la matriz q del ejemplo.
  %tol es el criterio de parada.
%Retorna el valor de m utilizado, el número de iteraciones realizadass y el porcentaje de error.
  %m es el tama˜no de sistema de ecuaciones a resolver.
  %k es el número de iteraciones realizadas.
  %error es el porcentaje de error alcanzado.
function [m, k, error]= pshss(iterMax, W, T, p, q, tol, m)
  w = 1;
  x = zeros(length(p),1);
  i = sqrt(-1);
  A = W + i*T;
  b = p + i*q;

  I = eye(size(A));

  for k=1:iterMax
    M = (w * W) + T;
    p1 = -i * (w*T - W) * x;
    p2 = (w-i)*b;
    n = p1 + p2;
    x = mldivide(M,n);

    error = norm(A*x - b);
    if  error <= tol
      break
    endif

  endfor
endfunction
