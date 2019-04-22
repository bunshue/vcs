clc;close all;clear all;

VR_SPEED_DUTY_MAX = 100;
VR_SPEED_DUTY_MIN = 25;
VR_MAX = 4.5;
VR_MIN = 0.5;

voltage=0:0.01:5;

for i=1:length(voltage)
	if(voltage(i)>=VR_MAX)
		vr_duty(i) = VR_SPEED_DUTY_MAX;
	elseif(voltage(i)<=VR_MIN)
		vr_duty(i) = 0;
    else
		vr_duty(i) = floor((voltage(i)-VR_MIN)/((VR_MAX-VR_MIN)/(VR_SPEED_DUTY_MAX-VR_SPEED_DUTY_MIN)))+VR_SPEED_DUTY_MIN;
    end
end
figure(1);
%bar(vr_duty,'linewidth',3)
plot(voltage,vr_duty,'linewidth',3)
axis([0 5 -10 110])
xlabel('VR voltage')
ylabel('PWM duty')

grid on;

input_pwm_duty=0:0.01:100;

for i=1:length(input_pwm_duty)
	if(input_pwm_duty(i)>=95)
        output_pwm_duty(i) = 100;
    elseif(input_pwm_duty(i)>=85)
        output_pwm_duty(i) = 90;
    elseif(input_pwm_duty(i)>=75)
        output_pwm_duty(i) = 80;
    elseif(input_pwm_duty(i)>=65)
        output_pwm_duty(i) = 70;
    elseif(input_pwm_duty(i)>=55)
        output_pwm_duty(i) = 60;
    elseif(input_pwm_duty(i)>=45)
        output_pwm_duty(i) = 50;
    elseif(input_pwm_duty(i)>=35)
        output_pwm_duty(i) = 40;
    elseif(input_pwm_duty(i)>=25)
        output_pwm_duty(i) = 30;
    elseif(input_pwm_duty(i)>=15)
        output_pwm_duty(i) = 20;
    elseif(input_pwm_duty(i)>=5)
        output_pwm_duty(i) = 10;
    else
        output_pwm_duty(i) = 0;
    end
end
figure(2);
%bar(vr_duty,'linewidth',3)
plot(input_pwm_duty,output_pwm_duty,'linewidth',3)
axis([-10 110 -10 110])
xlabel('¿é¤Jduty')
ylabel('¿é¥Xduty')
grid on;
