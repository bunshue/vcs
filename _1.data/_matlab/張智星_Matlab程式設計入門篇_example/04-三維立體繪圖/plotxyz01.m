x = linspace(-2, 2, 25);	% �b x �b [-2,2] ������ 25 �I  
y = linspace(-2, 2, 25);	% �b y �b [-2,2] ������ 25 �I  
[xx, yy] = meshgrid(x, y);	% xx �M yy ���O 25��25 ���x�}  
zz = xx.*exp(-xx.^2-yy.^2);	% �p���ƭȡAzz �]�O 25��25 ���x�}
mesh(xx, yy, zz);		% �e�X��������� 
%colormap(zeros(1,3));		% �H�¦�e�{  