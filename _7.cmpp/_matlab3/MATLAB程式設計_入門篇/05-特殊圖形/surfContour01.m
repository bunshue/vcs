x = linspace(-2*pi, 2*pi, 21);			% �b x �b [-2*pi, 2*pi] ������ 21 �I  
y = linspace(-1.5*pi, 1.5*pi, 31);		% �b y �b [-1.5*pi, 1.5*pi] ������ 31 �I  
[xx, yy] = meshgrid(x, y);			% xx �M yy ���O 21��31 ���x�}  
zz = sin(xx/2).*cos(yy);				% �p���ƭȡAzz �]�O 21��31 ���x�}
subplot(1,2,1)
surf(xx, yy, zz); axis image
subplot(1,2,2)
contour(xx, yy, zz); axis image