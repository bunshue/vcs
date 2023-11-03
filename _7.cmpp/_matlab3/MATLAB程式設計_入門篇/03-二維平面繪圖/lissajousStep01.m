t = linspace(0, 2*pi, 101);
m=1; n=2;
x=cos(m*t);
y=sin(n*t);
subplot(221); plot(t, x, 'marker', '.'); xlabel('t'); ylabel('x(t)'); grid on
set(gca, 'xlim', [min(t), max(t)]);
yLim1=get(gca, 'ylim');
circleH1=line(nan, nan, 'marker', 'o', 'color', 'r');
lineH1=line(nan, nan, 'color', 'r');
subplot(223); plot(t, y, 'marker', '.'); xlabel('t'); ylabel('y(t)'); grid on
set(gca, 'xlim', [min(t), max(t)]);
yLim2=get(gca, 'ylim');
circleH2=line(nan, nan, 'marker', 'o', 'color', 'r');
lineH2=line(nan, nan, 'color', 'r');
subplot(122); plot(x, y, 'marker', '.'); xlabel('x(t)'); ylabel('y(t)'); grid on
axis image
circleH3=line(nan, nan, 'marker', 'o', 'color', 'r');

for i=1:length(t)
	fprintf('Press any key to continue...'); pause; fprintf('\n');
	set(circleH1, 'xdata', t(i), 'ydata', x(i));
	set(lineH1, 'xdata', t(i)*[1 1], 'ydata', [yLim1(1), x(i)]);
	set(circleH2, 'xdata', t(i), 'ydata', y(i));
	set(lineH2, 'xdata', t(i)*[1 1], 'ydata', [yLim2(1), y(i)]);
	set(circleH3, 'xdata', x(i), 'ydata', y(i));
end