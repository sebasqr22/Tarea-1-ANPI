function pregunta5_E2()
  clc;
  disp("Método 4: QR y Eliminacion Gaussiana");
  disp("Caso 1:QR");
  tic;
  [W,T,b,m]=procedimiento(16);
  solucion_QR(W, T, real(b), imag(b))
  fprintf('Tiempo de ejecución: %f segundos\n', toc)
  disp("Caso 1:Eliminacion Gaussiana");
  tic;
  [W,T,b,m]=procedimiento(16);
  solucion_Gauss(W, T, real(b), imag(b))
  fprintf('Tiempo de ejecución: %f segundos\n', toc)




endfunction


function [W,T,b,m]=procedimiento(m)
   n = m^2;
  h = 1/(m+1);

  In = eye(n);
  Im = eye(m);

  tri = tridiago(m);
  Bm = (1/(h^2)) * tri;

  K = kron(Im,Bm) + kron(Bm,Im);

  W = K +  (-1) * In;
  T = 1 * In*i;

  A = W + i*T;

  b = ones(n,1);
  for j=1:n
    b1 = (1-i)*j;
    b2 = h*((j+1)^2);
    b(j) = b1/b2;
  endfor
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
