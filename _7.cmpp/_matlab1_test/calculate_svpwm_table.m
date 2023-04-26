%每10度一點，M由0.01、0.02、0.03、、1，共100表格

%七段式SVPWM
%每1度一點，M由0.01、0.02、0.03、、1，共100表格
clear,clc;
disp('UINT code SVPWM_TALBE_A[100][61] ={')
for i=1:1:100
	M=i/100;
	PWM_PERIOD=400;
	format compact
	theta=0:1:60;		%中間的1代表每次改變的角度
	duty_A=0.5+0.5*M*sind(60-theta)+0.5*M*sind(theta);
	duty_B=0.5-0.5*M*sind(60-theta)+0.5*M*sind(theta);
	duty_C=0.5-0.5*M*sind(60-theta)-0.5*M*sind(theta);
	pwm_a = floor(PWM_PERIOD* (1-duty_A));
	%pwm_b = floor(PWM_PERIOD* (1-duty_B));
	%pwm_c = floor(PWM_PERIOD* (1-duty_C));
	fprintf('{');
	for j=1:1:61
		if(pwm_a(j)>=100)
			fprintf('%d',pwm_a(j));
		else
			fprintf(' %d',pwm_a(j));
		end
		if(j==61)
			if(i==100)
				disp('}};');
			else
				disp('},');
			end
		else
			fprintf(', ');
		end
	end
end
disp('UINT code SVPWM_TALBE_B[100][61] ={')
for i=1:1:100
	M=i/100;
	PWM_PERIOD=400;
	format compact
	theta=0:1:60;		%中間的1代表每次改變的角度
	duty_A=0.5+0.5*M*sind(60-theta)+0.5*M*sind(theta);
	duty_B=0.5-0.5*M*sind(60-theta)+0.5*M*sind(theta);
	duty_C=0.5-0.5*M*sind(60-theta)-0.5*M*sind(theta);
	%pwm_a = floor(PWM_PERIOD* (1-duty_A));
	pwm_b = floor(PWM_PERIOD* (1-duty_B));
	%pwm_c = floor(PWM_PERIOD* (1-duty_C));
	fprintf('{');
	for j=1:1:61
		if(pwm_b(j)>=100)
			fprintf('%d',pwm_b(j));
		else
			fprintf(' %d',pwm_b(j));
		end
		if(j==61)
			if(i==100)
				disp('}};');
			else
				disp('},');
			end
		else
			fprintf(', ');
		end
	end
end

disp('UINT code SVPWM_TALBE_C[100][61] ={')
for i=1:1:100
	M=i/100;
	PWM_PERIOD=400;
	format compact
	theta=0:1:60;		%中間的1代表每次改變的角度
	duty_A=0.5+0.5*M*sind(60-theta)+0.5*M*sind(theta);
	duty_B=0.5-0.5*M*sind(60-theta)+0.5*M*sind(theta);
	duty_C=0.5-0.5*M*sind(60-theta)-0.5*M*sind(theta);
	%pwm_a = floor(PWM_PERIOD* (1-duty_A));
	%pwm_b = floor(PWM_PERIOD* (1-duty_B));
	pwm_c = floor(PWM_PERIOD* (1-duty_C));
	fprintf('{');
	for j=1:1:61
		if(pwm_c(j)>=100)
			fprintf('%d',pwm_c(j));
		else
			fprintf(' %d',pwm_c(j));
		end
		if(j==61)
			if(i==100)
				disp('}};');
			else
				disp('},');
			end
		else
			fprintf(', ');
		end
	end
end




使用：
fprintf('sum = %d\n',sum);
	disp('離開');










Tpwm=50us

T1=M*Tpwm*sin(60°-α)
T2=M*Tpwm*sin(α)
T0=Tpwm-T1-T2

dutyA=(T0/2+T2+T1)/Tpwm
dutyB=(T0/2+T2)/Tpwm
dutyC=(T0/2)/Tpwm

duty_A=0.5+0.5*M*sind(60-theta)+0.5*M*sind(theta)
duty_B=0.5-0.5*M*sind(60-theta)+0.5*M*sind(theta)
duty_C=0.5-0.5*M*sind(60-theta)-0.5*M*sind(theta)

pwm_a = PWM_PERIOD* (1-duty_A) = PWM_PERIOD* (0.5-0.5*M*sind(60-theta)-0.5*M*sind(theta))
pwm_b = PWM_PERIOD* (1-duty_B) = PWM_PERIOD* (0.5+0.5*M*sind(60-theta)-0.5*M*sind(theta))
pwm_c = PWM_PERIOD* (1-duty_C) = PWM_PERIOD* (0.5+0.5*M*sind(60-theta)+0.5*M*sind(theta))







dutyA(31)=75;dutyB(31)=50;dutyC(31)=25;
PWMA(31)=78;PWMB(31)=156;PWMC(31)=234;




theta=0:1:60;

%theta=30

M=0.7;PWM_PERIOD=400;

duty_A=0.5+0.5*M*sind(60-theta)+0.5*M*sind(theta)
duty_B=0.5-0.5*M*sind(60-theta)+0.5*M*sind(theta)
duty_C=0.5-0.5*M*sind(60-theta)-0.5*M*sind(theta)


pwm_a = floor(PWM_PERIOD* (1-duty_A))
pwm_b = floor(PWM_PERIOD* (1-duty_B))
pwm_c = floor(PWM_PERIOD* (1-duty_C))

plot(pwm_a,'r*-','LineWidth',2);hold on;
plot(pwm_b,'gs:','LineWidth',2);hold on;
plot(pwm_c,'bs:','LineWidth',2);hold on;

SVPWM_TALBE_A70 = [80,80,80,80,76,76,76,72,72,72,72,72,72,68,68,68,68,68,68,64,68,64,64,64,64,64,64,64,64,64,60,64,64,64,64,64,64,64,64,64,68,64,68,68,68,68,68,68,72,72,72,72,72,72,76,76,76,80,80,80,80];
SVPWM_TALBE_B70 = [320,320,316,312,308,304,300,296,292,288,284,280,276,272,268,264,260,256,252,248,244,240,236,232,228,220,220,212,212,208,200,196,192,188,184,180,176,172,164,164,160,156,152,148,144,140,132,128,128,124,116,116,108,104,104,100,92,92,88,84,80];
SVPWM_TALBE_C70 = [320,324,324,324,324,328,328,328,328,332,328,332,332,332,332,336,336,336,336,340,336,340,336,340,340,336,340,336,340,340,340,340,340,336,340,336,340,340,336,340,336,340,336,336,336,336,332,332,332,332,328,332,328,328,328,328,324,324,324,324,320];

plot(SVPWM_TALBE_A70,'k*-','LineWidth',2);hold on;
plot(SVPWM_TALBE_B70,'ks:','LineWidth',2);hold on;
plot(SVPWM_TALBE_C70,'ks:','LineWidth',2);hold on;



如果PWM_PERIOD固定為400，即20K。

每次M變換的時候，先去更新table，再套用table值。


const UINT sinetable100[] = {
0,  2,  3,  5,  7,  9, 10, 12, 14, 16, 17, 19, 21, 22, 24, 26, 28, 29, 31, 33, 34, 36, 37, 39, 41, 42, 44, 45, 47, 48, 50, 52, 53, 54, 56, 57, 59, 60, 62, 63, 64, 66, 67, 68, 69, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87};
/* matlab code for sine table : round((sind(0:60))*100)*/


Byte pwma[61]={};
Byte pwma[61]={};
Byte pwma[61]={};

plot(PWMA,'r*-','LineWidth',2);hold on;
plot(PWMB,'gs:','LineWidth',2);hold on;
plot(PWMC,'bs:','LineWidth',2);hold on;




