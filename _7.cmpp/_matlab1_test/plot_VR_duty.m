


clear,clc,clf
VR_SPEED_M_MAX=80;
VR_SPEED_M_MIN=10;
VR_MAX=4500;
VR_MIN=500;
voltage=1:1:5000;

for i=1:1:5000
    if (voltage(i)>=VR_MAX)
    	vr_duty(i) = VR_SPEED_M_MAX;
    elseif (voltage(i)<=VR_MIN)
    	vr_duty(i) = 0;
    else
    	vr_duty(i) = ((voltage(i)-VR_MIN)/((VR_MAX-VR_MIN)/(VR_SPEED_M_MAX-VR_SPEED_M_MIN)))+VR_SPEED_M_MIN;
    end
end
plot(voltage,vr_duty,'r')
xlabel('VR (mV)');
ylabel('svpwm-m');
axis([0 5000 0 100])
