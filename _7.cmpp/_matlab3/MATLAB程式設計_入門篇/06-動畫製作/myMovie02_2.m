close all
theta = linspace(0, 2*pi);
r1 = 3;
circle1 = r1*exp(sqrt(-1)*theta);	% �j��
plot(circle1), axis image

r2 = 1;
circle2 = r2*exp(sqrt(-1)*theta);	% �p��
center = r1+r2;
h = line(real(center+circle2), imag(center+circle2), 'EraseMode', 'xor', 'color', 'r');
axis([-5 5 -5 5]);			% �]�w�϶b���d��
n = 5;					% ��5��
theta1 = linspace(0, n*2*pi, n*2000);
for i = 1:length(theta1);
	center = (r1+r2)*exp(sqrt(-1)*(theta1(i)));
	set(h, 'xdata', real(center+circle2), 'ydata', imag(center+circle2));	% �]�w�p�ꪺ x, y �y��
	drawnow									% �ߧY�@��
end