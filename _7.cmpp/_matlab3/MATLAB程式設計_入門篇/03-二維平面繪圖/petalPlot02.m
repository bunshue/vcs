r=3;		% �p��b�|
R=10;		% �j��b�|
d=2;		% �������p���߶Z��
n=r/gcd(r, R);	% ���
t=linspace(0, n*2*pi, 1000);
c=R*exp(i*t);
% ����ä�u
c1=(R-r)*exp(i*t)+d*exp(i*(-R*t/r+t));
% �~��ä�u
c2=(R+r)*exp(i*t)+d*exp(i*(pi+R*t/r+t));
plot(real(c), imag(c), real(c1), imag(c1), real(c2), imag(c2));
axis image
title('����ä�u�]���^�M�~��ä�u�]����^');