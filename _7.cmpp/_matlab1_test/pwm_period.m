clc;close all;clear all;

IOSC=16e6;

PWM_period=100:10:2000;

for i=1:length(PWM_period)
    T(i)=1/IOSC*2*PWM_period(i)*1e6;
end
F=(1./T)*1e3;
%plotyy(PWM_period,T,PWM_period,F,'linewidth',3)
plotyy(PWM_period,T,PWM_period,F)
%axis([0 1000 0 1000])
xlabel('PWM period(point)')
ylabel('PWM period(usec)')
grid on;


        