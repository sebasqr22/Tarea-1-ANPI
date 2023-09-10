% Instituto Tecnologico de Costa Rica
% Ingenieria en Computadores
% Analisis Numerico Para Ingenieria, Tarea 1

% Metodo de Ostrowski Modificado
% Grupo: Sergio Rios, Sebastian Rojas, Luis Diego Araya , Andres Molina

% Entradas: filename=Nombre del archivo donde esté la Funcion f(x)=0,
%           x0= Valor inicial

% Salidas: k= Numero de iteraciones,
%          Raiz= Raiz de la funcion f,
%          Porcentaje de error

function [c] = modifiedOstrowski(filename, x0)
  tic;
  clc;
  x=x0;
  f=str2func(filename); % Convertir la funcion de string a funcion matematica
  iterMax=2500; % Maximo de iteraciones del metodo
  tol=10e-8; % Tolerancia especificada
  k=0; % Iteracion 0

  w = (x0 + 1)^(-1/8); % Definición de la función de peso utilizada por el metodo de Ostrowski Modificado

  while  k<iterMax % Comienza el ciclo iterativo
    k++; % Suma una iteracion al contador
    fx = f(x0); % X evaluada en la funcion f
    dfx=(f(x0 + eps) - f(x0)) / eps; % Aproximación de la derivada
    xnew = x0 - w * f(x0) / dfx; % X+1 con algoritmo de Ostrowski Modificado


    % Comprobación de la tolerancia
    if abs(xnew - x0) < tol
      break;
    end

    % Actualización de la aproximación
    x0 = xnew;

  endwhile
  if (k >= iterMax)
    printf('No se pudo resolver por Ostrowski Modificado');
  end

  printf('\n\n==============RESULTADO==============\n\n');
  printf('==============OSTROWSKI==============\n');
  printf('Iteracion: %d Valor inicial: %d Raiz: %d5  Porcentaje de error: %d\n',k,x,x0,max( abs(feval(f,x0)), abs(x0-xnew))*100);
  toc;
  end

