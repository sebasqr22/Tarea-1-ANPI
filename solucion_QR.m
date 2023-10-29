function solucion_QR(W,T,p,q)
  % Definir las matrices A y b según enunciado
  A=W+T*i;
  b=p+q*i;
  % Crear la matriz M y el vector d
  M=[real(A) -imag(A);imag(A) real(A)];
  d=[real(b);imag(b)];

  % Resuelve el sistema Mz = d usando factorización QR
  [Q,R]=metodoQR(M);

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
  x=u+v*i
  disp('ERROR =');
  disp(norm((A*x-b),2));
end
