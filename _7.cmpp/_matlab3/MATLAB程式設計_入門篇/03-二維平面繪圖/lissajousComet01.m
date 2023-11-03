colordef none
t = linspace(0, 4*pi, 20001);
m=3; n=5;
x=cos(m*t);
y=sin(n*t);
comet(x,y, 0.02);
colordef white