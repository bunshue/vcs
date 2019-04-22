clear,clc,clf,
fz=20e3;	%PWM freq = 20kHz
Tz=1/fz;

a=0.8;
alpha=30;
T1=Tz*a*sind(60-alpha)/sind(60);
T2=Tz*a*sind(alpha)/sind(60);
T0=Tz-(T1+T2);

Tzus=Tz*1e6;
T0us=T0*1e6;
T1us=T1*1e6;
T2us=T2*1e6;

T=[Tzus T0us T1us T2us];
PWM_C=(T0/2)/Tz;
PWM_B=((T0/2)+T2)/Tz;
PWM_A=((T0/2)+T2+T1)/Tz;
PWM_ABC=floor([PWM_A PWM_B PWM_C]*100);

alpha=30;
M=0.5;
T1=Tz*M*sind(60-alpha);
T2=Tz*M*sind(alpha);
T0=Tz-(T1+T2);

Tzus=Tz*1e6;
T0us=T0*1e6;
T1us=T1*1e6;
T2us=T2*1e6;

%T=[Tzus T0us T1us T2us]
PWM_C=(T0/2)/Tz;
PWM_B=((T0/2)+T2)/Tz;
PWM_A=((T0/2)+T2+T1)/Tz;
PWM_ABC=floor([PWM_A PWM_B PWM_C]*100)


