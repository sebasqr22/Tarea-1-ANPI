%Funcion que implementa computacionalmente el metodo PNHSS.
%Recibe las iteraciones maximas, W, T, p, q (que son vectores) y la toleracia
%Retorna el tama˜no de sistema de ecuaciones a resolver, la cantidad de iteraciones y el % de error.
function [m, k, error]= pnhss(iterMax, W, T, p, q, tol, m)
  w = 1;
  a = 1;
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
    x_media = mldivide(M,n);

    %parte 2
    M = a*I + w*W + T;
    p1 = (a*I - i*(w*T - W)) * x_media;
    p2 = (w-i)*b;
    n = p1 + p2;
    x = mldivide(M, n);

    error = norm(A*x - b);
    if  error <= tol
      break
    endif

  endfor
endfunction
