t = linspace(0, 2*pi, 1001);
for i=1:5
	subplot(2,5,i);
	polar(t, 1+cos(i*t));
	title(sprintf('r=1+cos(%d\\theta)', i));
end
for i=1:5
	subplot(2,5,5+i);
	polar(t, 1+sin(i*t));
	title(sprintf('r=1+sin(%d\\theta)', i));
end