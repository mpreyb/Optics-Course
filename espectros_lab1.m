
%espectros_lab1
% ÓPTICA - PRÁCTICA 1: Análisis espectral y medición del índice de refracción de un vidrio.
% @version MATLAB R2020b
%
% Otros archivos .m requeridos: ninguno
% Subfunciones: ninguna
% Archivos .MAT requeridos: "blue.mat","green.mat","helium.mat",
% "lamp.mat","laser.mat","laser.mat","red.mat","unknown.mat","white.mat"
%
% Autor: Maria Paula Rey B./Juan Esteban Ramirez
% email: mpreyb@eafit.edu.co/jeramirezm@eafit.edu.co
% Noviembre 2020; Última revisión: 14-Noviembre-2020

%------------------ BEGIN CODE ---------------------------
% ------------Gas desconocido----------------
unknown = readmatrix('desconocido_exc.xlsx');
lambda_1 = unknown(:, 1);
intensity_1 = unknown(:, 2);

figure('Name','Gas desconocido','NumberTitle','off');
plot(lambda_1,intensity_1);
xlabel('Longitud de onda (nm)');
ylabel('Intensidad (W/m^2)');
title('Espectro del gas desconocido');
hold on

% ------------Filtro azul----------------
blue = readmatrix('Filtro_azul_exc.xlsx');
lambda_2 = blue(:, 1);
intensity_2 = blue(:, 2);

figure('Name','Filtro azul','NumberTitle','off');
plot(lambda_2,intensity_2);
xlabel('Longitud de onda (nm)');
ylabel('Intensidad (W/m^2)');
title('Luz blanca con filtro de espectro de onda azul');
hold on

% ------------Filtro rojo----------------
red = readmatrix('Filtro_rojo_exc.xlsx');
lambda_3 = red(:, 1);
intensity_3 = red(:, 2);

figure('Name','Filtro rojo','NumberTitle','off');
plot(lambda_3,intensity_3);
xlabel('Longitud de onda (nm)');
ylabel('Intensidad (W/m^2)');
title('Luz blanca con filtro de espectro de onda roja');
hold on

% ------------Filtro verde----------------
green = readmatrix('Filtro_verde_exc.xlsx');
lambda_4 = green(:, 1);
intensity_4 = green(:, 2);

figure('Name','Filtro verde','NumberTitle','off');
plot(lambda_4,intensity_4);
xlabel('Longitud de onda (nm)');
ylabel('Intensidad (W/m^2)');
title('Luz blanca con filtro de espectro de onda verde');
hold on

% ------------Gas de Helio----------------
helium = readmatrix('Helio_exc.xlsx');
lambda_5 = helium(:, 1);
intensity_5 = helium(:, 2);

figure('Name','Helio','NumberTitle','off');
plot(lambda_5,intensity_5);
xlabel('Longitud de onda (nm)');
ylabel('Intensidad (W/m^2)');
title('Espectro de gas de Helio');
hold on

% ------------Lámpara----------------
lamp = readmatrix('Lampara_Lab_exc.xlsx');
lambda_6 = lamp(:, 1);
intensity_6 = lamp(:, 2);

figure('Name','Lámpara','NumberTitle','off');
plot(lambda_6,intensity_6);
xlabel('Longitud de onda (nm)');
ylabel('Intensidad (W/m^2)');
title('Espectro de luz de la lámpara');
hold on

% ------------Láser----------------
laser = readmatrix('Laser_exc.xlsx');
lambda_7 = laser(:, 1);
intensity_7 = laser(:, 2);

figure('Name','Láser','NumberTitle','off');
plot(lambda_7,intensity_7);
xlabel('Longitud de onda (nm)');
ylabel('Intensidad (W/m^2)');
title('Espectro del láser');
hold on

% ------------Luz blanca----------------
white = readmatrix('Luz_blanca_exc.xlsx');
lambda_8 = white(:, 1);
intensity_8 = white(:, 2);

figure('Name','Luz blanca','NumberTitle','off');
plot(lambda_8,intensity_8);
xlabel('Longitud de onda (nm)');
ylabel('Intensidad (W/m^2)');
title('Espectro de luz blanca');
hold on

%------------------ END OF CODE ---------------------------
