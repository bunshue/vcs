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

clear,clc,clf,
fz=20e3;	%PWM freq = 20kHz
Tz=1/fz;

M=0.4
alpha=0:10:50;
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
figure(1);
plot(alpha,PWM_AA,'r*-','LineWidth',5);hold on;
plot(alpha,PWM_BB,'gs:','LineWidth',5);hold on;
plot(alpha,PWM_CC,'b^-.','LineWidth',5);hold on;
axis([0 360 -10 110])
%title([ 'M = ', num2str(M)])
legend('PWM A','PWM B','PWM C')
xlabel('angle  (degree)')
ylabel('PWM duty')

alpha=60:10:110;
plot(alpha,fliplr(PWM_BB),'r*-','LineWidth',5);hold on;
plot(alpha,fliplr(PWM_AA),'gs:','LineWidth',5);hold on;
plot(alpha,fliplr(PWM_CC),'b^-.','LineWidth',5);hold on;

alpha=120:10:170;
plot(alpha,PWM_CC,'r*-','LineWidth',5);hold on;
plot(alpha,PWM_AA,'gs:','LineWidth',5);hold on;
plot(alpha,PWM_BB,'b^-.','LineWidth',5);hold on;

alpha=180:10:230;
plot(alpha,fliplr(PWM_CC),'r*-','LineWidth',5);hold on;
plot(alpha,fliplr(PWM_BB),'gs:','LineWidth',5);hold on;
plot(alpha,fliplr(PWM_AA),'b^-.','LineWidth',5);hold on;

alpha=240:10:290;
plot(alpha,PWM_BB,'r*-','LineWidth',5);hold on;
plot(alpha,PWM_CC,'gs:','LineWidth',5);hold on;
plot(alpha,PWM_AA,'b^-.','LineWidth',5);hold on;

alpha=300:10:350;
plot(alpha,fliplr(PWM_AA),'r*-','LineWidth',5);hold on;
plot(alpha,fliplr(PWM_CC),'gs:','LineWidth',5);hold on;
plot(alpha,fliplr(PWM_BB),'b^-.','LineWidth',5);hold on;

text(5,70,'M=0.4');
axis([0 360 20 80])
figure(2);

PWM_M40_A=[PWM_AA,fliplr(PWM_BB),PWM_CC,fliplr(PWM_CC),PWM_BB,fliplr(PWM_AA)];
PWM_M40_B=[PWM_BB,fliplr(PWM_AA),PWM_AA,fliplr(PWM_BB),PWM_CC,fliplr(PWM_CC)];
PWM_M40_C=[PWM_CC,fliplr(PWM_CC),PWM_BB,fliplr(PWM_AA),PWM_AA,fliplr(PWM_BB)];



























PWM=[PWM_AA;PWM_BB;PWM_CC]
bar(PWM','stacked')	%每個row疊在一起(由下而上)
xtk_label={'0','10','20','30','40','50','60'};	% 更改坐標軸名稱
set(gca,'xticklabel',xtk_label);
legend('PWM A','PWM B','PWM C')
xlabel('angle  (degree)')
ylabel('PWM duty')
text(0.5,130,'M=0.8');












