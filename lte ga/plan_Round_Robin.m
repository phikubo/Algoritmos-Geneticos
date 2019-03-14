% Simulador B�sico a Nivel de Sistema para LTE.
% Licencia academica, no comercial.
% Autor: Claudia Shirley Paz Arteaga, Eileen Johana Martinez G�mez
% Grupo de Radio e Inalambricas GRIAL
% Universidad del Cauca
% 2014

% Simulador B�sico a Nivel de Sistema para LTE con Planificadores de Recursos Radio Integrados.
% Licencia academica, no comercial.
% Autor: Dar�o Giraldo Medina, Diego Fernando Uribe Ante
% Grupo de Radio e Inalambricas GRIAL
% Universidad del Cauca
% 2015

% Simulador B�sico a Nivel de Sistema para LTE con Planificadores de Recursos Radio Integrados y T�cnicas de Re�so de Frecuencia.
% Licencia academica, no comercial.
% Autor: Mar�a Manuela Silva Zambrano, Valentina Giselle Moreno Parra
% Grupo de Radio e Inalambricas GRIAL
% Universidad del Cauca
% 2015

%%

function[prb_RR,prb_unused]=plan_Round_Robin(mi,tp_RR,prb,nue)

prb_RR=zeros(nue,mi);
p=zeros(1,mi);

for i=1:mi
p(1,i)=1/(tp_RR(:,i));
end

for i=1:mi
for x=1:nue
  
    prb_RR(x,i)= floor(prb/(nue));
end
end
prb_unused=prb-sum(prb_RR);
