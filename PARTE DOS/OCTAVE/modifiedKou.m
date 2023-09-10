% Instituto Tecnologico de Costa Rica
% Ingenieria en Computadores
% Analisis Numerico Para Ingenieria, Tarea 1

% Metodo de Kou Modificado
% Grupo: Sergio Rios, Sebastian Rojas, Luis Diego Araya , Andres Molina

% Entradas: filename=Nombre del archivo donde esté la Funcion f(x)=0,
%           x0= Valor inicial

% Salidas: k= Numero de iteraciones,
%          Raiz= Raiz de la funcion f,
%          Porcentaje de error

function x = modifiedKou(filename, x0)
  tic;
  clc;
  x=x0;
  f=str2func(filename); % Convertir la funcion de string a funcion matematica
  iterMax=2500; % Maximo de iteraciones del metodo
  tol=10e-8; % Tolerancia especificada
  k=0; % Iteracion 0

  while (k < iterMax)
    k++; % Suma una iteracion al contador
    g_k = (f(x0 + eps) - f(x0)) / eps; %Primera derivada
    h_k = (f(x0 + 2 * eps) - f(x0 + eps)) / eps; %Segunda derivada
    xnew= x0 - (f(x0) / (g_k + h_k)); % X+1 con algoritmo de Kou Modificado



    % Comprobación de la tolerancia
    if abs(x0-xnew) < tol
      break;
    endif

    x0 = xnew; % Actualización de la aproximación

  endwhile

  if (k >= iterMax)
    printf('No se pudo resolver por Kou Modificado');
  end
    printf('\n\n==============RESULTADO==============\n\n');
    printf('==============KOU==============\n');
    printf('Iteraciones: %d Valor inicial: %d Raiz: %d Porcentaje de error %d\n',k,x,x0,max( abs(feval(f,x0)), abs(x0-xnew))*100);
    toc;
    end

