clear all
clc
%% Three phase space vector pulse width modulation using generalised multiphase space vector aproach 
ma0= sqrt(3)/2; %% maximum modulation index
ma=ma0;         %% desired ma value
Vdc=563;        %% dc link voltage
Vsr=ma*Vdc;     %% space vector variation with ma   
f0=50;
%% v/f stretegy for 3ph im
if ma<=ma0
fmod=f0*ma/ma0;
else
    fmod=f0;
end
no_sample=48;   %%  no of samples
Ts=(1/fmod)/no_sample;  %% sampling time period
Vm=2/3*Vsr;            %% peak of phase voltage
alp=2*pi/3;             %% phase diff 120 degree

ts=0:Ts/100:2/fmod;    %% step time
Va=Vm*sin(2*pi*fmod*ts);
Vb=Vm*sin(2*pi*fmod*ts-alp);
Vc=Vm*sin(2*pi*fmod*ts-2*alp);
Vtri=Ts*(.5-2*asin(sin(2*pi*ts/Ts+pi/2))/(2*pi)); %% triangular wave generation
L=length(ts);

for i=1:1:L
    %% three phase to two phase transformation (clark transformation)
Vds(i)=(Va(i)+Vb(i)*cos(alp)+ Vc(i)*cos(2*alp) );
Vqs(i)=(Vb(i)*sin(alp)+ Vc(i)*sin(2*alp) );
%% sector indentification  
tht(i)=atan2(Vqs(i),Vds(i));
if tht(i) >= 0
    theta(i)=tht(i);
else
    theta(i)=2*pi+tht(i);
end

if theta(i)>=0 && theta(i)<alp/2
    Sn(i)=1;
elseif theta(i)>=alp/2 && theta(i)<alp
    Sn(i)=2;
elseif theta(i)>=alp && theta(i)<3/2*alp
    Sn(i)=3;
elseif theta(i)>=3/2*alp && theta(i)<2*alp
    Sn(i)=4;
elseif theta(i)>=2*alp && theta(i)<5/2*alp
    Sn(i)=5;
else Sn(i)=6;
end
%% selection of swithing vector for each sector
if Sn(i)==1
    v1=[1 ;0 ;0];  %4;   
    v2=[1 ;1 ;0];  %6;  
    v0=[1 ;1 ;1];
elseif Sn(i)==2
    v1=[1; 1; 0];  %6;  
    v2=[0; 1; 0];  %2;
    v0=[1; 1; 1];
elseif Sn(i)==3
    v1=[0; 1; 0];  %2;
    v2=[0; 1; 1];  %3;
    v0=[1; 1; 1];
elseif Sn(i)==4
    v1=[0; 1; 1];  %3;
    v2=[0; 0; 1];  %1
    v0=[1; 1; 1];
elseif Sn(i)==5
    v1=[0; 0; 1];   %1;
    v2=[1; 0; 1];   %5;
    v0=[1; 1; 1];
else
    v1=[1; 0; 1];  %5;
    v2=[1; 0; 0];  %4;
    v0=[1; 1; 1];  %0;
end

u=Sn(i);
%% using volt sec balance calcution of active timing vector 
An_inv=(Ts/(sin(pi/3)*Vdc))*[sin(u*pi/3) -cos(u*pi/3) ; -sin((u-1)*pi/3) cos((u-1)*pi/3) ];
Vref=[Vds(i); Vqs(i)];

tn=An_inv*Vref;

t0by2=(Ts-tn(1)-tn(2))/2;
t120=[tn(1);tn(2); t0by2];

V120=[v1 v2 v0];
%% calculation for tga gating time period for each leg
tgx(:,i) = (V120)*(t120);
tga(i)=tgx(1,i);
tgb(i)=tgx(2,i);
tgc(i)=tgx(3,i);

%% generation of switching function SA SB SC
 if tgx(1,i)>= Vtri(i)
     sA(i)=1;
 else 
     sA(i)=-1;
 end
 if tgx(2,i)>= Vtri(i)
     sB(i)=1;
 else
     sB(i)=-1;
 end
 if tgx(3,i)>= Vtri(i)
     sC(i)=1;
 else
     sC(i)=-1;
 end
 %% invertor modelign
 Van(i)=1/3*(2*sA(i)-sB(i)-sC(i))*Vdc/2;
 Vbn(i)=1/3*(2*sB(i)-sA(i)-sC(i))*Vdc/2;
 Vcn(i)=1/3*(2*sC(i)-sB(i)-sA(i))*Vdc/2;

end
    %% fft analysis of output voltage
k=0:L-1;
f=k*fmod/4;
Vft=fft(Van);
Vmag=abs(Vft);
m=1:1:L;

%% normalise harmonic spectrum
h=stem(f(m),Vmag(m)/max(Vmag),'k');

set(get(h,'BaseLine'),'LineStyle','-.')
axis([0 5000 0 1])
set(h,'MarkerFaceColor',[0 0 1],'Marker','.','Color',[0 0 0])
title('harmonics spectrum of phase voltage');
xlabel('frequecy');
ylabel('normalised harmonic voltage');
figure;
plot(ts,Van)
hold on
title('ts vs Van');
xlabel('Time in seconds');
ylabel('Volts');
figure
plot(ts,Sn);
hold on
title('ts vs Sn');
xlabel('Time in seconds');
ylabel('Sector no');
figure
plot(ts,tga,ts,tgb,ts,tgc);
hold on
title('ts vs tga tgb tgc');
xlabel('Time in seconds');
ylabel('tga');
figure
plot(ts,Vtri);
hold on
title('ts vs Vtri');
xlabel('Time in seconds');
ylabel('Vtri');
figure
plot(ts,tga,ts,Vtri);
hold on
title('ts vs tga Vtri');
xlabel('Time in seconds');
ylabel('Volts');
figure
plot(ts,sA);
hold on
title('ts vs SA');
xlabel('Time in seconds');
ylabel('SA');


%% rohit chandan email: chandan.rho@gmail.com