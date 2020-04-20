colordef none
theta = linspace(0, 4*pi, 10001);
r=cos(4*theta);
x=r.*cos(theta);
y=r.*sin(theta);
comet(x, y, 0.04);
colordef white