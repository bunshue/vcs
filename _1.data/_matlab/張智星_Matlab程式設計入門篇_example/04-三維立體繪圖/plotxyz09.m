x = 6*rand(100,1)-3;		% x ������ [-3, 3] �� 100 �I�ü�  
y = 6*rand(100,1)-3;		% y ������ [-3, 3] �� 100 �I�ü�  
z = peaks(x, y);			% z �� peaks ���O���ͪ� 100 �I��X  
[X, Y] = meshgrid(-3:0.1:3);  
Z = griddata(x, y, z, X, Y, 'cubic');	% �� cubic ���t�k�i�椺�t  
meshc(X, Y, Z);
hold on
plot3(x, y, z, '.', 'MarkerSize', 16);	% �ޥX 100 �Ө���  
hold off
axis tight