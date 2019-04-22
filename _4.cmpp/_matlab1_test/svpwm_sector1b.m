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

M=0.1
alpha=0:10:60;
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
%PWM_ABC=floor([PWM_A PWM_B PWM_C]*100)
PWM_AA=floor(PWM_A*100)
PWM_BB=floor(PWM_B*100)
PWM_CC=floor(PWM_C*100)

PWM_AA2=[PWM_AA(1:7) fliplr(PWM_BB(1:6))	(PWM_CC(2:7))	(PWM_CC(2:7))       (PWM_BB(2:7)) (PWM_AA(2:7))];
PWM_BB2=[PWM_BB(1:7) (PWM_AA(2:7))	(PWM_AA(2:7))	fliplr(PWM_BB(1:6))	(PWM_CC(2:7))       (PWM_CC(2:7))];
PWM_CC2=[PWM_CC(1:7) (PWM_CC(2:7))	(PWM_BB(2:7)) 	(PWM_AA(2:7))       (PWM_AA(2:7)) fliplr(PWM_BB(1:6))];

beta=0:10:360;

plot(beta,PWM_AA2,'r*-','LineWidth',5);hold on;
plot(beta,PWM_BB2,'g*:','LineWidth',5);hold on;
plot(beta,PWM_CC2,'b*-.','LineWidth',5);hold on;

axis([0 380 -10 110])
%title([ 'M = ', num2str(M)])
legend('PWM A','PWM B','PWM C')
xlabel('angle  (degree)')
ylabel('PWM duty')
grid on

text(5,98,'M=1');
M
PWM_AA2
PWM_BB2
PWM_CC2


