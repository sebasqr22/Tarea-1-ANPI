%Función que llama al método del ejemplo número 1 del artículo A parameterized SHSS iteration method for a class of complex symmetric system of linear equations.
%No recibe parámetros.
%Retorna el valor de m utilizado, el número de iteraciones realizadass y el porcentaje de error, para cada método implementado con la estructura solicitada por el profesor.
  %m es el tama˜no de sistema de ecuaciones aresolver.
  %k es el número de iteraciones realizadas.
  %error es el porcentaje de error alcanzado.
function pregunta5_E1()
  clc;
  disp("--------------------------Ejemplo1--------------------------");

  disp("Método 1:HSS");
  disp("Caso 1:");
  tic;
  [W,T,b,m]=procedimiento(16);
  [m, iteraciones, error] =hss(5000, W, T, real(b), imag(b), 10^(-6)*norm(b), m)
  fprintf('Tiempo de ejecución: %f segundos\n', toc)

  disp("Caso 2:");
  tic;
  [W,T,b,m]=procedimiento(32);
  [m, error, iteraciones] = hss(5000, W, T, real(b), imag(b), 10^(-6)*norm(b), m)
  fprintf('Tiempo de ejecución: %f segundos\n', toc)

  disp("Caso 3:");
  tic;
  [W,T,b,m]=procedimiento(64);
  [m, error, iteraciones] = hss(5000, W, T, real(b), imag(b), 10^(-6)*norm(b), m)
  fprintf('Tiempo de ejecución: %f segundos\n', toc)

  disp("Caso 4:");
  tic;
  [W,T,b,m]=procedimiento(128),
  [m, error, iteraciones] = hss(5000, W, T, real(b), imag(b), 10^(-6)*norm(b), m)
  fprintf('Tiempo de ejecución: %f segundos\n', toc)

  disp("Caso 5:");
  tic;
  [W,T,b,m]=procedimiento(256);
  [m, error, iteraciones] = hss(5000, W, T, real(b), imag(b), 10^(-6)*norm(b), m)
  fprintf('Tiempo de ejecución: %f segundos\n', toc)

  disp("Método 2: PNHSS y PSHSS");
  disp("Caso 1: PNHSS");
  tic;
  [W,T,b,m]=procedimiento(16);
  [m, iteraciones, error] = pnhss(5000, W, T, real(b), imag(b), 10^(-6)*norm(b),m)
  fprintf('Tiempo de ejecución: %f segundos\n', toc)
  disp("Caso 1: PSHSS");
  tic;
  [W,T,b,m]=procedimiento(16);
  [m, iteraciones, error] = pshss(5000, W, T, real(b), imag(b), 10^(-6)*norm(b),m)
  fprintf('Tiempo de ejecución: %f segundos\n', toc)

  disp("Caso 2: PNHSS");
  tic;
  [W,T,b,m]=procedimiento(32);
  [m, iteraciones, error] = pnhss(5000, W, T, real(b), imag(b), 10^(-6)*norm(b),m)
  fprintf('Tiempo de ejecución: %f segundos\n', toc)
  disp("Caso 2: PSHSS");
  tic;
  [W,T,b,m]=procedimiento(32);
  [m, iteraciones, error] = pshss(5000, W, T, real(b), imag(b), 10^(-6)*norm(b),m)
  fprintf('Tiempo de ejecución: %f segundos\n', toc)

  disp("Caso 3: PNHSS");
  tic;
  [W,T,b,m]=procedimiento(64);
  [m, iteraciones, error] = pnhss(5000, W, T, real(b), imag(b), 10^(-6)*norm(b),m)
  fprintf('Tiempo de ejecución: %f segundos\n', toc)
  disp("Caso 3: PSHSS");
  tic;
  [W,T,b,m]=procedimiento(64);
  [m, iteraciones, error] = pshss(5000, W, T, real(b), imag(b), 10^(-6)*norm(b),m)
  fprintf('Tiempo de ejecución: %f segundos\n', toc)

  disp("Caso 4: PNHSS");
  tic;
  [W,T,b,m]=procedimiento(128);
  [m, iteraciones, error] = pnhss(5000, W, T, real(b), imag(b), 10^(-6)*norm(b),m)
  fprintf('Tiempo de ejecución: %f segundos\n', toc)
  disp("Caso 4: PSHSS");
  tic;
  [W,T,b,m]=procedimiento(128);
  [m, iteraciones, error] = pshss(5000, W, T, real(b), imag(b), 10^(-6)*norm(b),m)
  fprintf('Tiempo de ejecución: %f segundos\n', toc)

  disp("Caso 5: PNHSS");
  tic;
  [W,T,b,m]=procedimiento(256);
  [m, iteraciones, error] = pnhss(5000, W, T, real(b), imag(b), 10^(-6)*norm(b),m)
  fprintf('Tiempo de ejecución: %f segundos\n', toc)
  disp("Caso 5: PSHSS");
  tic;
  [W,T,b,m]=procedimiento(256);
  [m, iteraciones, error] = pshss(5000, W, T, real(b), imag(b), 10^(-6)*norm(b),m)
  fprintf('Tiempo de ejecución: %f segundos\n', toc)

  disp("Método 3: MHSS");
  disp("Caso 1:");
  tic;
  [W,T,b,m]=procedimiento(16);
  [m, error, iteraciones] = mhss(5000, W, T, real(b), imag(b), 10^(-6)*norm(b), m)
  fprintf('Tiempo de ejecución: %f segundos\n', toc)

  disp("Caso 2:");
  tic;
  [W,T,b,m]=procedimiento(32);
  [m, error, iteraciones] = mhss(5000, W, T, real(b), imag(b), 10^(-6)*norm(b), m)
  fprintf('Tiempo de ejecución: %f segundos\n', toc)

  disp("Caso 3:");
  tic;
  [W,T,b,m]=procedimiento(64);
  [m, error, iteraciones] = mhss(5000, W, T, real(b), imag(b), 10^(-6)*norm(b), m)
  fprintf('Tiempo de ejecución: %f segundos\n', toc)

  disp("Caso 4:");
  tic;
  [W,T,b,m]=procedimiento(128),
  [m, error, iteraciones] = mhss(5000, W, T, real(b), imag(b), 10^(-6)*norm(b), m)
  fprintf('Tiempo de ejecución: %f segundos\n', toc)

  disp("Caso 5:");
  tic;
  [W,T,b,m]=procedimiento(156);
  [m, error, iteraciones] = mhss(5000, W, T, real(b), imag(b), 10^(-6)*norm(b), m)
  fprintf('Tiempo de ejecución: %f segundos\n', toc)

  disp("Método 4: QR y Eliminacion Gaussiana");
  disp("Caso 1:QR");
  tic;
  [W,T,b,m]=procedimiento(16);
  solucion_QR(W, T, real(b), imag(b),m)
  fprintf('Tiempo de ejecución: %f segundos\n', toc)
  disp("Caso 1:Eliminacion Gaussiana");
  tic;
  [W,T,b,m]=procedimiento(16);
  solucion_Gauss(W, T, real(b), imag(b),m)
  fprintf('Tiempo de ejecución: %f segundos\n', toc)

  disp("Caso 2:QR");
  tic;
  [W,T,b,m]=procedimiento(32);
  solucion_QR(W, T, real(b), imag(b),m)
  fprintf('Tiempo de ejecución: %f segundos\n', toc)
  disp("Caso 2:Eliminacion Gaussiana");
  tic;
  [W,T,b,m]=procedimiento(32);
  solucion_Gauss(W, T, real(b), imag(b),m)
  fprintf('Tiempo de ejecución: %f segundos\n', toc)

  disp("Caso 3:QR");
  tic;
  [W,T,b,m]=procedimiento(64);
  solucion_QR(W, T, real(b), imag(b),m)
  fprintf('Tiempo de ejecución: %f segundos\n', toc)
  disp("Caso 3:Eliminacion Gaussiana");
  tic;
  [W,T,b,m]=procedimiento(64);
  solucion_Gauss(W, T, real(b), imag(b),m)
  fprintf('Tiempo de ejecución: %f segundos\n', toc)

  disp("Caso 4:QR");
  tic;
  [W,T,b,m]=procedimiento(128);
  solucion_QR(W, T, real(b), imag(b),m)
  fprintf('Tiempo de ejecución: %f segundos\n', toc)
  disp("Caso 4:Eliminacion Gaussiana");
  tic;
  [W,T,b,m]=procedimiento(128);
  solucion_Gauss(W, T, real(b), imag(b),m)
  fprintf('Tiempo de ejecución: %f segundos\n', toc)

  disp("Caso 5:QR");
  tic;
  [W,T,b,m]=procedimiento(256);
  solucion_QR(W, T, real(b), imag(b),m)
  fprintf('Tiempo de ejecución: %f segundos\n', toc)
  disp("Caso 5:Eliminacion Gaussiana");
  tic;
  [W,T,b,m]=procedimiento(256);
  solucion_Gauss(W, T, real(b), imag(b),m)
  fprintf('Tiempo de ejecución: %f segundos\n', toc)

endfunction

%Función que calcula el método iterativo del ejemplo número 1 del artículo A parameterized SHSS iteration method for a class of complex symmetric system of linear equations.
%Recibe como parámetros el tama˜no de sistema de ecuaciones a resolver m.
%Retorna a la matiz W y T, a los vectores p y q, y el tama˜no de sistema de ecuaciones a resolver m.
function [W,T,b,m]= procedimiento(m)
  n = m^2;
  h = 1/(m+1);

  In = eye(n);
  Im = eye(m);

  tri = tridiago(m);
  Bm = (1/(h^2)) * tri;

  K = kron(Im,Bm) + kron(Bm,Im);

  W = K + ((3-sqrt(3))/h) * In;
  T = K + ((3+sqrt(3))/h) * In;

  A = W + i*T;

  b = ones(n,1);
  for j=1:n
    b1 = (1-i)*j;
    b2 = h*((j+1)^2);
    b(j) = b1/b2;
  endfor

  %[x, k, error] = PNHSS(1000, W, T, real(b), imag(b), 10^(-6)*norm(b))
endfunction

%Función que genera una matriz tridiagonal, donde la digonal principal tenga el valor de 2, y las diagonales adyacentes igual a -1.
%Recibe como parámetro n que es el tama˜no de sistema de ecuaciones a resolver al cuadrado
%Retorna la matriz tridiagonal con la estructira solicitada.
function G=tridiago(n)
  G=zeros(n);
  %Primera fila
  G(1,1)=2; G(1,2)=-1;
  %Ultima Fila
  G(n,n)=2; G(n,n-1)=-1;

  for i=2:n-1
    G(i,i)=2; G(i,i-1)=-1; G(i,i+1)=-1;
  end
endfunction
