% Instituto Tecnologico de Costa Rica
% Ingenieria en Computadores
% Analisis Numerico Para Ingenieria, Tarea 2

% Pregunta4 Métodos de Factorización QR y Eliminación Gaussiana
% Grupo: Sergio Rios, Sebastian Quesada, Luis Diego Araya , Andres Molina

%Función que llama a los métodos para encontrar la solución del ejemplo de la tarea a traves de los métodos QR y eliminación Gaussiana.
%No recibe parámetros.
%Retorna la solución al problemma del ejemplo del la pregunta 4.
function pregunta4 ()
  clc;
  W=[12 -2 6 -2; -2 5 2 1; 6 2 9 -2; -2 1 -2 1];
  T=[6 2 7 2; 2 7 1 1; 7 1 9 0; 2 1 0 10];
  p=[9;-7;-5;7];
  q=[12;-4;17;-2];
  solucionQR(W,T,p,q);
  solucionGauss(W,T,p,q)

end

%Función que calcula la solución a través del método QR.
%Recibe W, T, p, q y m.
%Retorna la solución al sistema de ecuaciones planteado.
function solucionQR(W,T,p,q)
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

%Función que calcula las matrices R y Q de A a través del método QR.
%Recibe la matriz A, que es la matriz que queremos factorizar a través del método QR.
%Retorna las matrices Q y R, que son la factorización de la matriz A con el método QR.
function [Q,R]=metodoQR(A)
  [m,n]=size(A);
  U=zeros(m);
  Q=zeros(m);

  U(:,1)=A(:,1);
  Q(:,1)=U(:,1)/norm(U(:,1),2);
  k=2;
  [m,n]=size(A);
  while k<=m
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

%Función que calcula la solución a través del método de eliminación Gaussiana.
%Recibe W, T, p, q y m.
%Retorna la solución al sistema de ecuaciones planteado
function solucionGauss(W,T,p,q)
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
  x=u+v*i
  disp('ERROR =');
  disp(norm((A*x-b),2));
end
