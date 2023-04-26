clear,clc,clf;
pwm(1:1:61)=30;
subplot(211);bar(pwm);axis([1 60 0 40]);

for i=1:1:61
spwm(i)=30*sind(i*3);
end
subplot(212);bar(spwm);axis([1 60 0 40]);

