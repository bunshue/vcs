function regStar(n)

if nargin<1, n=7; end

vertices=[1];
for i=1:n
	step=2*pi*floor(n/2)/n;
	vertices=[vertices, exp(i*step*sqrt(-1))];
end
plot(vertices, '-o');

% µe¥~±µ¶ê
hold on
theta=linspace(0, 2*pi);
plot(cos(theta), sin(theta), '-r');
hold off

axis image