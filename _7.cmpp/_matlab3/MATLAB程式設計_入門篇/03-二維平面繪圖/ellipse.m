function ellipse(a, b)

if nargin<1, a=7; end
if nargin<2, b=2; end

% µe¾ò¶ê
theta=linspace(0, 2*pi, 101);
plot(a*cos(theta), b*sin(theta));

axis image