function solucion_QR(W,T,p,q,m)
  % Definir las matrices A y b según enunciado
  A=W+T*i;
  b=p+q*i;
  % Crear la matriz M y el vector d
  M=[real(A) -imag(A);imag(A) real(A)];
  d=[real(b);imag(b)];

  % Resuelve el sistema Mz = d usando factorización QR
  [Q,R]=metodo_QR(M);

  n = length(d);
  z = zeros(n, 1);

  % Realiza la sustitución hacia atrás con el resultado del QR
  z(n) = (Q(:,n)' * d) / R(n, n);
  for k = n-1:-1:1
      z(k) = (Q(:,k)' * d - R(k, k+1:n) * z(k+1:n)) / R(k, k);
  end

  % La solución z contiene los valores reales u y v
  u = z(1:n/2);
  v = z(n/2+1:n);
  % Obtener solución x
  x=u+v*i;
  disp('m =');
  disp(m);
  disp('ERROR =');
  disp(norm((A*x-b),2));

end

function [Q,R]=metodo_QR(A)
  [r,n]=size(A);
  U=zeros(r);
  Q=zeros(r);

  U(:,1)=A(:,1);
  Q(:,1)=U(:,1)/norm(U(:,1),2);
  k=2;
  [r,n]=size(A);
  while k<=r
    y=0;
    for j=1:(k-1)
      y+=dot(A(:,k), Q(:,j))*Q(:,j);
    endfor

    U(:,k)=A(:,k)- y;
    Q(:,k)=U(:,k)/norm(U(:,k),2);
    k++;
  endwhile
  R=transpose(Q)*A;
end


