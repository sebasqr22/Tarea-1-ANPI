%Función que llama al método iterativo PNHSS y PS*HSS para el ejemplo planteado en el enunciado de la tarea.
%no recibe parámetros.
%Retorna el llamado a las funciones PNHSS y PS*HSS.
function pregunta2()
  clc;
  iterMax = 1000;
  W = [12 -2 6 -2;-2 5 2 1;6 2 9 -2;-2 1 -2 1];
  T = [6 2 7 2; 2 7 1 1; 7 1 9 0; 2 1 0 10];
  p = [9;-7;-5;7];
  q = [12;-4;17;-2];
  tol = 10^(-12);

  display("Método PNHSS:")
  [x, k, error] = PNHSS(iterMax, W, T, p, q, tol)

  display("\nMétodo PS*HSS:")
  [x, k, error] = PSHSS(iterMax, W, T, p, q, tol)
endfunction

%funcion que implementa el metodo PNHSS
%recibe las iteraciones maximas, W, T, p, q (que son vectores) y la toleracia
%retorna el valor x, cantidad de iteraciones y el %de error
function [x, k, error]= PNHSS(iterMax, W, T, p, q, tol)
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

%funcion que implementa el metodo PSHSS
%recibe las iteraciones maximas, W, T, p, q (que son vectores) y la toleracia
%retorna el valor x, cantidad de iteraciones y el %de error
function [x, k, error]= PSHSS(iterMax, W, T, p, q, tol)
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
