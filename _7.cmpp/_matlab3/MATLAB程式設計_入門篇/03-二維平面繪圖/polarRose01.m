t = linspace(0, 2*pi, 1001);
for i=1:5
	subplot(2,5,i);
	polar(t, cos(i*t));
	title(sprintf('r=cos(%d\\theta)', i));
end
for i=1:5
	subplot(2,5,5+i);
	polar(t, sin(i*t));
	title(sprintf('r=sin(%d\\theta)', i));
end