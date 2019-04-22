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


alpha=0:10:60;
%M=1.154
M=1
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

plot(alpha,PWM_AA,'r*-','LineWidth',5);hold on;
plot(alpha,PWM_BB,'gs:','LineWidth',5);hold on;
plot(alpha,PWM_CC,'b^-.','LineWidth',5);hold on;
axis([0 60 -10 110])
%title([ 'M = ', num2str(M)])
legend('PWM A','PWM B','PWM C')
xlabel('angle  (degree)')
ylabel('PWM duty')

M=0.8
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

plot(alpha,PWM_AA,'r*-','LineWidth',3);hold on;
plot(alpha,PWM_BB,'gs:','LineWidth',3);hold on;
plot(alpha,PWM_CC,'b^-.','LineWidth',3);hold on;
axis([0 60 -10 110])
%title([ 'M = ', num2str(M)])
%legend('PWM A','PWM B','PWM C')
%xlabel('angle')
%ylabel('PWM duty')

M=0.6
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

plot(alpha,PWM_AA,'r*-','LineWidth',2);hold on;
plot(alpha,PWM_BB,'gs:','LineWidth',2);hold on;
plot(alpha,PWM_CC,'b^-.','LineWidth',2);hold on;
axis([0 60 -10 110])
%title([ 'M = ', num2str(M)])
%legend('PWM A','PWM B','PWM C')
%xlabel('angle')
%ylabel('PWM duty')

text(5,98,'M=1');
text(5,88,'M=0.8');
text(5,79,'M=0.6');

