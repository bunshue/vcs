% 擺線的動畫, Roger Jang, 20050208

x = linspace(0, 5*pi, 2000);
theta = linspace(0, 2*pi);
r = 1;
circle = j+r*exp(sqrt(-1)*theta);
subplot(2,1,1);
circleH=plot(circle); axis image
set(circleH, 'erase', 'xor');
axis([min(x)-r, max(x)+r, -0.5, 2*r+0.5]);
dot1H=line(0, 0, 'marker', 'o', 'color', 'k', 'erase', 'xor');
dot2H=line(0, 0, 'marker', '.', 'color', 'r', 'erase', 'none');

for i=1:length(x)
	set(circleH, 'xdata', x(i)+real(circle));
	angle=-pi/2-x(i);
	set(dot1H, 'xdata', x(i)+cos(angle), 'ydata', r+sin(angle));
	set(dot2H, 'xdata', x(i)+cos(angle), 'ydata', r+sin(angle));
%	line('xdata', x(i)+cos(angle), 'ydata', r+sin(angle), 'color', 'r', 'marker', '.');
	drawnow
end