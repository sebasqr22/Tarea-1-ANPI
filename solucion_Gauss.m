%Función que calcula la solución a través del método de eliminación Gaussiana.
%Recibe W, T, p, q y m.
%Retorna la solución al sistema de ecuaciones planteado.
function solucion_Gauss(W,T,p,q,m)
  % Definir las matrices A y b según enunciado
  A = W+T*i;
  b = p+q*i;

  % Crear la matriz M y el vector d
  M = [real(A), -imag(A); imag(A), real(A)];
  d = [real(b); imag(b)];

  % Resuelve el sistema Mz = d usando eliminación Gaussiana
  n = length(d);
  z = zeros(n, 1);

  % Eliminación Gaussiana
  for k = 1:n
      for j = k+1:n
          factor = M(j, k) / M(k, k);
          M(j, k:n) = M(j, k:n) - factor * M(k, k:n);
          d(j) = d(j) - factor * d(k);
      end
  end

  % Sustitución hacia atrás
  z(n) = d(n) / M(n, n);
  for k = n-1:-1:1
      z(k) = (d(k) - M(k, k+1:n) * z(k+1:n)) / M(k, k);
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
