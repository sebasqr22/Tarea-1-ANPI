% Instituto Tecnologico de Costa Rica
% Ingenieria en Computadores
% Analisis Numerico Para Ingenieria, Tarea 1

% Metodo de la falsa posicion
% Grupo: Sergio Rios, Sebastian Rojas, Luis Diego Araya , Andres Molina

% Entradas: filename=Nombre del archivo donde esté la Funcion f(x)=0,
%           a= Valor inicial de rango,
%           b= valor final de rango

% Salidas: k= Numero de iteraciones,
%          Raiz= Raiz de la funcion f,
%          Porcentaje de error

function [c] =falsaPos(filename,a,b)
  tic;
  clc;
  a0=a;
  b0=b;
  f=str2func(filename); % Convertir la funcion de string a funcion matematica
  iterMax=2500; % Maximo de iteraciones del metodo
  tol=10e-8; % Tolerancia especificada
  k=0; % Iteracion 0
  ya=feval(f,a); % valor inicial de rango evaluada en f
  yb=feval(f,b); % valor final de rango evaluada en f
  x_ant=0;
  if ya*yb<=0  %Verifica el teorema de Bolzano

    %Primera iteracion para obtener el primer dato a usar en el porcentaje de error
    k=k+1; % Suma una iteracion al contador
    c= b- ( (b-a)/(yb-ya))*yb; % Obtiene el punto del rango más cercano al cero
    yc=feval(f,c); % Evalua el punto obtenido en la funcion f% Evalua el punto obtenido en la funcion f

    % Verificacion del teorema de Bolzano en los subintervalos [a,c] y [c,b]
    if ya*yc==0
      a=b;
    elseif ya*yc<0
      b=c;
      yb=yc;
    else
      a=c;
      ya=yc;
    endif
    x_ant=c;

    while  k<iterMax % Comienza el ciclo iterativo
      k=k+1; % Suma una iteracion al contador
      c= b- ( (b-a)/(yb-ya))*yb; % Obtiene el punto del rango más cercano al cero
      yc=feval(f,c); % Evalua el punto obtenido en la funcion f% Evalua el punto obtenido en la funcion f

      % Verificacion del teorema de Bolzano en los subintervalos [a,c] y [c,b]
      if ya*yc==0
        a=b;
      elseif ya*yc<0
        b=c;
        yb=yc;

      else
        a=c;
        ya=yc;

      endif

    if abs(c-x_ant)<tol
      break;
    endif
    x_ant=c;

    endwhile

    printf('\n==============RESULTADO==============\n\n');
    printf('==============FALSA POSICION==============\n');
    printf('Iteraciones: %d Valores iniciales: a: %d b: %d Raiz: %d Porcentaje de error:%d\n',k,a0,b0,c,max( abs(feval(f,c)), abs(c-x_ant))*100);
    toc;

  else
    % Si el intervalo dado no cumple Bolzano
    printf('El intervalo dado no cumple el teorema de Bolzano, por favor cambie el intervalo');
  endif

  end
