t = 0:0.1:4*pi;
y = exp(-t/5).*sin(t);
h = plot(t, y);			% h �����u������
set(h, 'Linewidth', 3);		% �N���u�e�קאּ 3
set(h, 'Marker', 'o');		% �N���u���u�Ч令�p���
set(h, 'MarkerSize', 20);	% �N�u�Ъ��j�p�令 20