t=0:0.4:4*pi;
h=plot(t, exp(-t/5).*sin(t));			% h �����u������
set(h, 'Marker', 'diamond', 'MarkerSize', 15, 'MarkerFaceColor', 'r');	% �N�u�Ч令�٧ΡB�u�Фj�p�令 15�B�u�Ъ����令����
fprintf('MATLAB version = %s\n', version);
get(h)		% �C�X h ���Ҧ��ʽ�