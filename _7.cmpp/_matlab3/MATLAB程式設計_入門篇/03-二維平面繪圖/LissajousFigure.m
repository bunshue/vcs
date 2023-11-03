t=linspace(0, 2*pi, 1000);

subplot(2,2,1);
m=1; n=1;
x=cos(m*t);
y=sin(n*t);
plot(x, y); title('m=1, n=1'); axis image

subplot(2,2,2);
m=3; n=2;
x=cos(m*t);
y=sin(n*t);
plot(x, y); title('m=3, n=2'); axis image

subplot(2,2,3);
m=2; n=7;
x=cos(m*t);
y=sin(n*t);
plot(x, y); title('m=2, n=7'); axis image

subplot(2,2,4);
m=10; n=11;
x=cos(m*t);
y=sin(n*t);
plot(x, y); title('m=10, n=11'); axis image