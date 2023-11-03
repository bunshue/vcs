close all
theta = linspace(0, 2*pi);
r1 = 3;
x1 = r1*cos(theta);
y1 = r1*sin(theta);
plot(x1, y1), axis image				% �j��

r2 = 1;
center = (r1+r2)*[1, 0];
x2 = r2*cos(theta);
y2 = r2*sin(theta);
h = line(center(1)+x2, center(2)+y2, 'EraseMode', 'xor', 'color', 'r');		% �p��
axis([-5 5 -5 5]);			% �]�w�϶b���d��
n = 5;					% ��5��
theta1 = linspace(0, n*2*pi, n*2000);
for i = 1:length(theta1);
	center = (r1+r2)*[cos(theta1(i)), sin(theta1(i))];
	set(h, 'xdata', center(1)+x2, 'ydata', center(2)+y2);		% �]�w�p�ꪺ x, y �y��
	drawnow								% �ߧY�@��
end