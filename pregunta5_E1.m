function pregunta5_E1()
  clc;
  disp("--------------------------Ejemplo1--------------------------");
  disp("Método 1:HSS");
  disp("Caso 1:");
  tic;
  [W,T,b,m]=procedimiento(16);
  [m, iteraciones, error] =hss(5000, W, T, real(b), imag(b), 10^(-6)*norm(b))
  fprintf('Tiempo de ejecución: %f segundos\n', toc)
  disp("Caso 2:");
  tic;
  [W,T,b,m]=procedimiento(32);
  [m, error, iteraciones] = hss(5000, W, T, real(b), imag(b), 10^(-6)*norm(b))
  fprintf('Tiempo de ejecución: %f segundos\n', toc)
  disp("Caso 3:");
  tic;
  [W,T,b,m]=procedimiento(64);
  [m, error, iteraciones] = hss(5000, W, T, real(b), imag(b), 10^(-6)*norm(b))
  fprintf('Tiempo de ejecución: %f segundos\n', toc)
  disp("Caso 4:");
  tic;
  %[W,T,b,m]=procedimiento(128),
  %[m, error, iteraciones] = hss(5000, W, T, real(b), imag(b), 10^(-6)*norm(b))
  fprintf('Tiempo de ejecución: %f segundos\n', toc)
  disp("Caso 5:");
  tic;
  %[W,T,b,m]=procedimiento(256);
  %[m, error, iteraciones] = hss(5000, W, T, real(b), imag(b), 10^(-6)*norm(b))
  fprintf('Tiempo de ejecución: %f segundos\n', toc)


  disp("Método 2: PNHSS y PSHSS");
  disp("Caso 1: PNHSS");
  tic;
  [W,T,b,m]=procedimiento(16);
  [m, error, iteraciones] = PNHSS(5000, W, T, real(b), imag(b), 10^(-6)*norm(b))
  fprintf('Tiempo de ejecución: %f segundos\n', toc)
  disp("Caso 1: PSHSS");
  tic;
  [W,T,b,m]=procedimiento(16);
  [m, error, iteraciones] = PNHSS(5000, W, T, real(b), imag(b), 10^(-6)*norm(b))
  fprintf('Tiempo de ejecución: %f segundos\n', toc)

  disp("Caso 2: PNHSS");
  tic;
  [W,T,b,m]=procedimiento(32);
  [m, error, iteraciones] = PNHSS(5000, W, T, real(b), imag(b), 10^(-6)*norm(b))
  fprintf('Tiempo de ejecución: %f segundos\n', toc)
  disp("Caso 2: PSHSS");
  tic;
  [W,T,b,m]=procedimiento(32);
  [m, error, iteraciones] = PNHSS(5000, W, T, real(b), imag(b), 10^(-6)*norm(b))
  fprintf('Tiempo de ejecución: %f segundos\n', toc)


  disp("Caso 3: PNHSS");
  tic;
  [W,T,b,m]=procedimiento(64);
  [m, error, iteraciones] = PNHSS(5000, W, T, real(b), imag(b), 10^(-6)*norm(b))
  fprintf('Tiempo de ejecución: %f segundos\n', toc)
  disp("Caso 3: PSHSS");
  tic;
  [W,T,b,m]=procedimiento(64);
  [m, error, iteraciones] = PNHSS(5000, W, T, real(b), imag(b), 10^(-6)*norm(b))
  fprintf('Tiempo de ejecución: %f segundos\n', toc)


  disp("Caso 4: PNHSS");
  tic;
  [W,T,b,m]=procedimiento(128);
  [m, error, iteraciones] = PNHSS(5000, W, T, real(b), imag(b), 10^(-6)*norm(b))
  fprintf('Tiempo de ejecución: %f segundos\n', toc)
  disp("Caso 4: PSHSS");
  tic;
  [W,T,b,m]=procedimiento(128);
  [m, error, iteraciones] = PNHSS(5000, W, T, real(b), imag(b), 10^(-6)*norm(b))
  fprintf('Tiempo de ejecución: %f segundos\n', toc)


  disp("Caso 5: PNHSS");
  tic;
  [W,T,b,m]=procedimiento(256);
  [m, error, iteraciones] = PNHSS(5000, W, T, real(b), imag(b), 10^(-6)*norm(b))
  fprintf('Tiempo de ejecución: %f segundos\n', toc)
  disp("Caso 5: PSHSS");
  tic;
  [W,T,b,m]=procedimiento(256);
  [m, error, iteraciones] = PNHSS(5000, W, T, real(b), imag(b), 10^(-6)*norm(b))
  fprintf('Tiempo de ejecución: %f segundos\n', toc)


  disp("Método 3: MHSS");
  disp("Caso 1:");
  tic;
  [W,T,b,m]=procedimiento(16);
  [m, error, iteraciones] = Pregunta3(5000, W, T, real(b), imag(b), 10^(-6)*norm(b), m)
  fprintf('Tiempo de ejecución: %f segundos\n', toc)
  disp("Caso 2:");
  tic;
  [W,T,b,m]=procedimiento(32);
  [m, error, iteraciones] = Pregunta3(5000, W, T, real(b), imag(b), 10^(-6)*norm(b), m)
  fprintf('Tiempo de ejecución: %f segundos\n', toc)
  disp("Caso 3:");
  tic;
  [W,T,b,m]=procedimiento(64);
  [m, error, iteraciones] = Pregunta3(5000, W, T, real(b), imag(b), 10^(-6)*norm(b), m)
  fprintf('Tiempo de ejecución: %f segundos\n', toc)
  disp("Caso 4:");
  tic;
  %[W,T,b,m]=procedimiento(128),
  %[m, error, iteraciones] = Pregunta3(5000, W, T, real(b), imag(b), 10^(-6)*norm(b), m)
  fprintf('Tiempo de ejecución: %f segundos\n', toc)
  disp("Caso 5:");
  tic;
  %[W,T,b,m]=procedimiento(156);
  %[m, error, iteraciones] = Pregunta3(5000, W, T, real(b), imag(b), 10^(-6)*norm(b), m)
  fprintf('Tiempo de ejecución: %f segundos\n', toc)

  disp("Método 4: QR y Eliminacion Gaussiana");
  disp("Caso 1:QR");
  tic;
  [W,T,b,m]=procedimiento(16);
  [m, error, iteraciones] = solucionQR(5000, W, T, real(b), imag(b), 10^(-6)*norm(b))
  fprintf('Tiempo de ejecución: %f segundos\n', toc)
  disp("Caso 1:Eliminacion Gaussiana");
  tic;
  [W,T,b,m]=procedimiento(16);
  [m, error, iteraciones] = solucionGauss(5000, W, T, real(b), imag(b), 10^(-6)*norm(b))
  fprintf('Tiempo de ejecución: %f segundos\n', toc)


  disp("Caso 2:QR");
  tic;
  [W,T,b,m]=procedimiento(32);
  [m, error, iteraciones] = solucionQR(5000, W, T, real(b), imag(b), 10^(-6)*norm(b))
  fprintf('Tiempo de ejecución: %f segundos\n', toc)
  disp("Caso 2:Eliminacion Gaussiana");
  tic;
  [W,T,b,m]=procedimiento(32);
  [m, error, iteraciones] = solucionGauss(5000, W, T, real(b), imag(b), 10^(-6)*norm(b))
  fprintf('Tiempo de ejecución: %f segundos\n', toc)


  disp("Caso 3:QR");
  tic;
  [W,T,b,m]=procedimiento(64);
  [m, error, iteraciones] = solucionQR(5000, W, T, real(b), imag(b), 10^(-6)*norm(b))
  fprintf('Tiempo de ejecución: %f segundos\n', toc)
  disp("Caso 3:Eliminacion Gaussiana");
  tic;
  [W,T,b,m]=procedimiento(64);
  [m, error, iteraciones] = solucionGauss(5000, W, T, real(b), imag(b), 10^(-6)*norm(b))
  fprintf('Tiempo de ejecución: %f segundos\n', toc)


  disp("Caso 4:QR");
  tic;
  [W,T,b,m]=procedimiento(128);
  [m, error, iteraciones] = solucionQR(5000, W, T, real(b), imag(b), 10^(-6)*norm(b))
  fprintf('Tiempo de ejecución: %f segundos\n', toc)
  disp("Caso 4:Eliminacion Gaussiana");
  tic;
  [W,T,b,m]=procedimiento(128);
  [m, error, iteraciones] = solucionGauss(5000, W, T, real(b), imag(b), 10^(-6)*norm(b))
  fprintf('Tiempo de ejecución: %f segundos\n', toc)


  disp("Caso 5:QR");
  tic;
  [W,T,b,m]=procedimiento(256);
  [m, error, iteraciones] = solucionQR(5000, W, T, real(b), imag(b), 10^(-6)*norm(b))
  fprintf('Tiempo de ejecución: %f segundos\n', toc)
  disp("Caso 5:Eliminacion Gaussiana");
  tic;
  [W,T,b,m]=procedimiento(256);
  [m, error, iteraciones] = solucionGauss(5000, W, T, real(b), imag(b), 10^(-6)*norm(b))
  fprintf('Tiempo de ejecución: %f segundos\n', toc)


endfunction




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
