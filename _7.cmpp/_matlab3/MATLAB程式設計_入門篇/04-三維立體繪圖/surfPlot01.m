x = linspace(-2, 2, 21);		% �b x �b [-2,2] ������ 21 �I  
y = linspace(-1, 1, 21);		% �b y �b [-1,1] ������ 21 �I  
[xx, yy] = meshgrid(x, y);		% xx �M yy ���O 21��21 ���x�}  
zz = xx.*exp(-xx.^2-yy.^2);		% �p���ƭȡAzz �]�O 21��21 ���x�}
subplot(1,3,1)
surf(xx, yy, zz); axis image
subplot(1,3,2)
surf(xx, yy, zz, gradient(zz)); axis image
subplot(1,3,3)
surf(xx, yy, zz, del2(zz)); axis image