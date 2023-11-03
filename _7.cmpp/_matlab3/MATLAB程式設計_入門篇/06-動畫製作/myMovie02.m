close all
theta = linspace(0, 2*pi);
r1 = 3;
x1 = r1*cos(theta);
y1 = r1*sin(theta);
plot(x1, y1), axis image				% 大圓

r2 = 1;
center = (r1+r2)*[1, 0];
x2 = r2*cos(theta);
y2 = r2*sin(theta);
h = line(center(1)+x2, center(2)+y2, 'EraseMode', 'xor', 'color', 'r');		% 小圓
axis([-5 5 -5 5]);			% 設定圖軸的範圍
n = 5;					% 轉5圈
theta1 = linspace(0, n*2*pi, n*2000);
for i = 1:length(theta1);
	center = (r1+r2)*[cos(theta1(i)), sin(theta1(i))];
	set(h, 'xdata', center(1)+x2, 'ydata', center(2)+y2);		% 設定小圓的 x, y 座標
	drawnow								% 立即作圖
end