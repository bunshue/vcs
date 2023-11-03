r=3;		% 小圓半徑
R=10;		% 大圓半徑
d=2;		% 筆心離小圓圓心距離
n=r/gcd(r, R);	% 圈數
t=linspace(0, n*2*pi, 1000);
c=R*exp(i*t);
% 內花瓣線
c1=(R-r)*exp(i*t)+d*exp(i*(-R*t/r+t));
% 外花瓣線
c2=(R+r)*exp(i*t)+d*exp(i*(pi+R*t/r+t));
plot(real(c), imag(c), real(c1), imag(c1), real(c2), imag(c2));
axis image
title('內花瓣線（綠色）和外花瓣線（紅色）');