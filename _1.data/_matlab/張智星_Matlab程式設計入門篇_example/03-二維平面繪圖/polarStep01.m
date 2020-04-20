t = linspace(0, 2*pi, 101);
r=cos(2*t);
subplot(121); plot(t, r, 'marker', '.'); xlabel('\theta'); ylabel('r(\theta)'); grid on
set(gca, 'xlim', [min(t), max(t)]);
yLim1=get(gca, 'ylim');
circleH1=line(nan, nan, 'marker', 'o', 'color', 'r');
lineH1=line(nan, nan, 'color', 'r');
subplot(122);
h=polar(t, r); set(h, 'marker', '.');
grid on
circleH2=line(nan, nan, 'marker', 'o', 'color', 'r');
angleH=line(nan, nan, 'color', 'r');
lineH2=line(nan, nan, 'color', 'm');
z=r.*exp(sqrt(-1)*t);
x=real(z); y=imag(z);

for i=1:length(t)
	fprintf('Press any key to continue...'); pause; fprintf('\n');
	set(circleH1, 'xdata', t(i), 'ydata', r(i));
	set(lineH1, 'xdata', t(i)*[1 1], 'ydata', [yLim1(1), r(i)]);
	set(circleH2, 'xdata', x(i), 'ydata', y(i));
	len=norm([x(i), y(i)]);
	set(angleH, 'xdata', [0, cos(t(i))], 'ydata', [0, sin(t(i))]);
	set(lineH2, 'xdata', [0 x(i)], 'ydata', [0, y(i)]);
end