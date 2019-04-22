clc;close all;clear all;

VR_SPEED_RPM_MAX = 3600;
VR_SPEED_RPM_MIN = 300;
VR_MAX = 4.5;
VR_MIN = 0.5;

voltage=0:0.01:5;

for i=1:length(voltage)
	if(voltage(i)>=VR_MAX)
		target_speed(i) = VR_SPEED_RPM_MAX;
	elseif(voltage(i)<=VR_MIN)
		target_speed(i) = 0;
    else
		target_speed(i) = floor((voltage(i)-VR_MIN)/((VR_MAX-VR_MIN)/(VR_SPEED_RPM_MAX-VR_SPEED_RPM_MIN)))+VR_SPEED_RPM_MIN;
    end
end
figure(1);
%bar(target_speed,'linewidth',3)
plot(voltage,target_speed,'linewidth',3)
axis([0 5 -10 VR_SPEED_RPM_MAX+100])
xlabel('VR voltage')
ylabel('target speed')

