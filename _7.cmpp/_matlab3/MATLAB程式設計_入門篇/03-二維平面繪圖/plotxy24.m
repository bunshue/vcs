theta = linspace(0, 4*pi, 30);  
rho = 10;  
[x, y] = pol2cart(theta, rho);	% �ѷ��y���ഫ�ܪ����y��  
feather(x, y);	% ø�s�Ф��
axis image