R=5;		% 大圓半徑
r=2;		% 小圓半徑
n=r/gcd(r, R);	% 圈數
t=linspace(0, n*2*pi, 1000);
c=R*exp(i*t);
% 內花瓣線
c1=(R-r)*exp(i*t)+r*exp(i*(-R*t/r+t));
% 外花瓣線
c2=(R+r)*exp(i*t)+r*exp(i*(pi+R*t/r+t));
plot(real(c), imag(c), real(c1), imag(c1), real(c2), imag(c2));
axis image
title('內花瓣線（綠色）和外花瓣線（紅色）');