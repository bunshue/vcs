%傅利葉級數

%t = 0:.0001:1;
t = 0:.02:50;
f = 1;

n = 1;
A= 4/(pi*n);
y1 = A*sin(n*t);

n = 3;
A= 4/(pi*n);
y3 = A*sin(n*t);

n = 5;
A= 4/(pi*n);
y5 = A*sin(n*t);


n = 7;
A= 4/(pi*n);
y7 = A*sin(n*t);

n = 9;
A= 4/(pi*n);
y9 = A*sin(n*t);

n = 11;
A= 4/(pi*n);
y11 = A*sin(n*t);

n = 13;
A= 4/(pi*n);
y13 = A*sin(n*t);

n = 15;
A= 4/(pi*n);
y15 = A*sin(n*t);

n = 17;
A= 4/(pi*n);
y17 = A*sin(n*t);

n = 19;
A= 4/(pi*n);
y19 = A*sin(n*t);

n = 21;
A= 4/(pi*n);
y21 = A*sin(n*t);

n = 23;
A= 4/(pi*n);
y23 = A*sin(n*t);


y = y1+y3+y5+y7+y9+y11;

subplot(511)
plot(y1(1:2000))
subplot(512)
plot(y3(1:2000))
subplot(513)
plot(y5(1:2000))
subplot(514)
plot(y7(1:2000))
subplot(515)
plot(y(1:2000))


figure()
%plot(y1(1:2000));hold on;
%plot(y3(1:2000));hold on;
%plot(y5(1:2000));hold on;
%plot(y7(1:2000));hold on;



yr = y1+y3;
yg = y1+y3+y5+y7+y9+y11;
yb = y1+y3+y5+y7+y9+y11+y13+y15;
yk = y1+y3+y5+y7+y9+y11+y13+y15+y17+y19+y21+y23;

plot(yr(1:500),'r');hold on;
plot(yg(1:500),'g');hold on;
plot(yb(1:500),'b');hold on;
plot(yk(1:500),'k');hold on;

