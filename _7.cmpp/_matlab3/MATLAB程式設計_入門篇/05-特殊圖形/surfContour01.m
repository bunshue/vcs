x = linspace(-2*pi, 2*pi, 21);			% 在 x 軸 [-2*pi, 2*pi] 之間取 21 點  
y = linspace(-1.5*pi, 1.5*pi, 31);		% 在 y 軸 [-1.5*pi, 1.5*pi] 之間取 31 點  
[xx, yy] = meshgrid(x, y);			% xx 和 yy 都是 21×31 的矩陣  
zz = sin(xx/2).*cos(yy);				% 計算函數值，zz 也是 21×31 的矩陣
subplot(1,2,1)
surf(xx, yy, zz); axis image
subplot(1,2,2)
contour(xx, yy, zz); axis image