t=linspace(0, 2*pi, 1000);

subplot(2,2,1);
m=1; n=2;
x=cos(m*t);
y=sin(n*t);
plot(x, y); title('(a)'); axis image

subplot(2,2,2);
m=2; n=1;
x=cos(m*t);
y=sin(n*t);
plot(x, y); title('(b)'); axis image

subplot(2,2,3);
m=2; n=3;
x=cos(m*t);
y=sin(n*t);
plot(x, y); title('(c)'); axis image

subplot(2,2,4);
m=3; n=2;
x=cos(m*t);
y=sin(n*t);
plot(x, y); title('(d)'); axis image