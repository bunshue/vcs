clc;close all;clear all;

VM = 2.3;

A=2.3;

HA_base = 25;
CMPVTH = HA_base-13.5;
CMPVTH2 = HA_base-20.5;

ideal_base = HA_base-16;

real_base = HA_base-17.3

HB_base = HA_base - 1.2;
HC_base = HA_base - 2.4;
U_base = HA_base-5;
V_base = U_base - VM-0.2;
W_base = U_base - (VM+0.2)*2;

t=1:1:720;
for i=1:1:720
    if (mod(i,360) <= 180)
    	HA(i)=1;
    elseif (mod(i,360) <= 360)
    	HA(i)=0;
    else
    	HA(i)=3;
    end
end

for i=1:1:720
    if (mod(i,360) <= 120)
    	HB(i)=0;
    elseif (mod(i,360) <= 300)
    	HB(i)=1;
    elseif (mod(i,360) <= 360)
    	HB(i)=0;
    else
    	HB(i)=3;
    end
end

for i=1:1:720
    if (mod(i,360) <= 60)
    	HC(i)=1;
    elseif (mod(i,360) <= 240)
    	HC(i)=0;
    elseif (mod(i,360) <= 360)
    	HC(i)=1;
    end
end

for i=1:1:720
    if (mod(i,360) <= 120)
    	if(mod(i,2)==0)
    	    U(i)=0;
    	else
            U(i)=VM;
    	end
    elseif (mod(i,360) <= 180)
    	if(mod(i,2)==0)
    	    U(i)=VM;
    	else
    	    U(i)=VM*1/3+(mod(i,360)-120)*1/3*VM/60;
    	end
    elseif (mod(i,360) <= 300)
        U(i)=VM;
    elseif (mod(i,360) <= 360)
    	if(mod(i,2)==0)
    	    U(i)=VM;
    	else
    	    U(i)=VM*2/3-(mod(i,360)-300)*1/3*VM/60;
    	end
    end
end

for i=1:1:720
    if (mod(i,360) <= 60)
        V(i)=VM;
    elseif (mod(i,360) <= 120)
    	if(mod(i,2)==0)
    	    V(i)=VM;
    	else
    	    V(i)=VM*2/3-(mod(i,360)-60)*1/3*VM/60;
        end
    elseif (mod(i,360) <= 240)
        if(mod(i,2)==0)
    	    V(i)=0;
    	else
            V(i)=VM;
    	end
    elseif (mod(i,360) <= 300)
        if(mod(i,2)==0)
    	    V(i)=VM;
    	else
    	    V(i)=VM*1/3+(mod(i,360)-240)*1/3*VM/60;
    	end
    elseif (mod(i,360) <= 360)
   	    V(i)=VM;
    end
end

for i=1:1:720
    if (mod(i,360) <= 60)
    	if(mod(i,2)==0)
    	    W(i)=VM;
    	else
    	    W(i)=VM*1/3+(mod(i,360)-0)*1/3*VM/60;
    	end
    elseif (mod(i,360) <= 180)
        W(i)=VM;
    elseif (mod(i,360) <= 240)
    	if(mod(i,2)==0)
    	    W(i)=VM;
    	else
    	    W(i)=VM*2/3-(mod(i,360)-180)*1/3*VM/60;
    	end
    elseif (mod(i,360) <= 360)
        if(mod(i,2)==0)
    	    W(i)=0;
    	else
            W(i)=VM;
    	end
    end
end

cmpb=A*sind(t+180);
cmpc=A*sind(t-120+180);
cmpd=A*sind(t-240+180);

cmpbb=A*sind(t+180+30);
cmpcc=A*sind(t-120+180+30);
cmpdd=A*sind(t-240+180+30);

HA(1) = 0;
HC(420) = 0;

HA=HA+HA_base;
HB=HB+HB_base;
HC=HC+HC_base;
U=U+U_base;
V=V+V_base;
W=W+W_base;

cmpb=cmpb+CMPVTH;
cmpc=cmpc+CMPVTH;
cmpd=cmpd+CMPVTH;

cmpbb=cmpbb+CMPVTH2;
cmpcc=cmpcc+CMPVTH2;
cmpdd=cmpdd+CMPVTH2;

hold on;

line([60 60],[8.5 100],'LineWidth',1,'Color','c')
line([120 120],[8.5 100],'LineWidth',1,'Color','c')
line([180 180],[8.5 100],'LineWidth',1,'Color','c')
line([240 240],[8.5 100],'LineWidth',1,'Color','c')
line([300 300],[8.5 100],'LineWidth',1,'Color','c')
line([360 360],[8.5 100],'LineWidth',1,'Color','c')
line([420 420],[8.5 100],'LineWidth',1,'Color','c')
line([480 480],[8.5 100],'LineWidth',1,'Color','c')
line([540 540],[8.5 100],'LineWidth',1,'Color','c')
line([600 600],[8.5 100],'LineWidth',1,'Color','c')
line([660 660],[8.5 100],'LineWidth',1,'Color','c')

line([30 30],[0 8.5],'LineWidth',1,'Color','c')
line([90 90],[0 8.5],'LineWidth',1,'Color','c')
line([150 150],[0 8.5],'LineWidth',1,'Color','c')
line([210 210],[0 8.5],'LineWidth',1,'Color','c')
line([270 270],[0 8.5],'LineWidth',1,'Color','c')
line([330 330],[0 8.5],'LineWidth',1,'Color','c')
line([390 390],[0 8.5],'LineWidth',1,'Color','c')
line([450 450],[0 8.5],'LineWidth',1,'Color','c')
line([510 510],[0 8.5],'LineWidth',1,'Color','c')
line([570 570],[0 8.5],'LineWidth',1,'Color','c')
line([630 630],[0 8.5],'LineWidth',1,'Color','c')

line([0 720],[HA_base HA_base],'LineWidth',1,'Color','c')
line([0 720],[HB_base HB_base],'LineWidth',1,'Color','c')
line([0 720],[HC_base HC_base],'LineWidth',1,'Color','c')
line([0 720],[U_base U_base],'LineWidth',1,'Color','c')
line([0 720],[V_base V_base],'LineWidth',1,'Color','c')
line([0 720],[W_base W_base],'LineWidth',1,'Color','c')

line([0 720],[CMPVTH CMPVTH],'LineWidth',4,'Color','m')

line([0 720],[CMPVTH2 CMPVTH2],'LineWidth',4,'Color','m')

plot(t,HA,'r-','LineWidth',4);
plot(t,HB,'g-','LineWidth',4);
plot(t,HC,'b-','LineWidth',4);
plot(t,U,'r-','LineWidth',3);
plot(t,V,'g-','LineWidth',3);
plot(t,W,'b-','LineWidth',3);
plot(t,cmpb,'r-','LineWidth',3);
plot(t,cmpc,'g-','LineWidth',3);
plot(t,cmpd,'b-','LineWidth',3);
plot(t,cmpbb,'r-','LineWidth',3);
plot(t,cmpcc,'g-','LineWidth',3);
plot(t,cmpdd,'b-','LineWidth',3);

text(3,HA_base+1.3,'五 101','Color','r');
text(63,HA_base+1.3,'四 100','Color','r');
text(123,HA_base+1.3,'六 110','Color','r');
text(183,HA_base+1.3,'二 010','Color','r');
text(243,HA_base+1.3,'三 011','Color','r');
text(303,HA_base+1.3,'一 001','Color','r');

text(53,CMPVTH-1,'W上','FontSize',20,'Color','blue');
text(113,CMPVTH-1,'V下','FontSize',20,'Color','green');
text(173,CMPVTH-1,'U上','FontSize',20,'Color','red');
text(233,CMPVTH-1,'W下','FontSize',20,'Color','blue');
text(293,CMPVTH-1,'V上','FontSize',20,'Color','green');
text(353,CMPVTH-1,'U下','FontSize',20,'Color','red');

text(53-30,CMPVTH2-1,'W上','FontSize',20,'Color','blue');
text(113-30,CMPVTH2-1,'V下','FontSize',20,'Color','green');
text(173-30,CMPVTH2-1,'U上','FontSize',20,'Color','red');
text(233-30,CMPVTH2-1,'W下','FontSize',20,'Color','blue');
text(293-30,CMPVTH2-1,'V上','FontSize',20,'Color','green');
text(353-30,CMPVTH2-1,'U下','FontSize',20,'Color','red');

text(10,HA_base+0.5,'HA','FontSize',20,'Color','red');
text(10,HB_base+0.5,'HB','FontSize',20,'Color','green');
text(10,HC_base+0.5,'HC','FontSize',20,'Color','blue');

text(10,U_base+1,'U','FontSize',20,'Color','black');
text(10,V_base+1,'V','FontSize',20,'Color','green');
text(10,W_base+1,'W','FontSize',20,'Color','black');

text(20,CMPVTH+0.4,'CMPVTH','FontSize',20,'Color','m');
text(40,CMPVTH2-0.6,'CMPVTH','FontSize',20,'Color','m');

text(8,CMPVTH-0.7,'CMPB','FontSize',20,'Color','r');
text(8,CMPVTH+1.8,'CMPC','FontSize',20,'Color','g');
text(8,CMPVTH-2.1,'CMPD','FontSize',20,'Color','b');

text(8,CMPVTH2-1.8,'CMPB','FontSize',20,'Color','r');
text(8,CMPVTH2+2.7,'CMPC','FontSize',20,'Color','g');
text(8,CMPVTH2+0.5,'CMPD','FontSize',20,'Color','b');

line([0 0],[CMPVTH-0.5 CMPVTH+0.5],'LineWidth',2,'Color','r')
line([60 60],[CMPVTH-0.5 CMPVTH+0.5],'LineWidth',2,'Color','r')
line([120 120],[CMPVTH-0.5 CMPVTH+0.5],'LineWidth',2,'Color','r')
line([180 180],[CMPVTH-0.5 CMPVTH+0.5],'LineWidth',2,'Color','r')
line([240 240],[CMPVTH-0.5 CMPVTH+0.5],'LineWidth',2,'Color','r')
line([300 300],[CMPVTH-0.5 CMPVTH+0.5],'LineWidth',2,'Color','r')
line([360 360],[CMPVTH-0.5 CMPVTH+0.5],'LineWidth',2,'Color','r')

line([0+30 0+30],[CMPVTH2-0.5 CMPVTH2+0.5],'LineWidth',2,'Color','r')
line([60+30 60+30],[CMPVTH2-0.5 CMPVTH2+0.5],'LineWidth',2,'Color','r')
line([120+30 120+30],[CMPVTH2-0.5 CMPVTH2+0.5],'LineWidth',2,'Color','r')
line([180+30 180+30],[CMPVTH2-0.5 CMPVTH2+0.5],'LineWidth',2,'Color','r')
line([240+30 240+30],[CMPVTH2-0.5 CMPVTH2+0.5],'LineWidth',2,'Color','r')
line([300+30 300+30],[CMPVTH2-0.5 CMPVTH2+0.5],'LineWidth',2,'Color','r')
line([360+30 360+30],[CMPVTH2-0.5 CMPVTH2+0.5],'LineWidth',2,'Color','r')

text(60-12,CMPVTH-2.5,'CMPD','FontSize',20,'Color','b');
text(120-12,CMPVTH-2.5,'CMPC','FontSize',20,'Color','g');
text(180-12,CMPVTH-2.5,'CMPB','FontSize',20,'Color','r');
text(240-12,CMPVTH-2.5,'CMPD','FontSize',20,'Color','b');
text(300-12,CMPVTH-2.5,'CMPC','FontSize',20,'Color','g');
text(360-12,CMPVTH-2.5,'CMPB','FontSize',20,'Color','r');

text(60-9,CMPVTH-3.2,'五 四','FontSize',20,'Color','b');
text(120-9,CMPVTH-3.2,'四 六','FontSize',20,'Color','g');
text(180-9,CMPVTH-3.2,'六 二','FontSize',20,'Color','r');
text(240-9,CMPVTH-3.2,'二 三','FontSize',20,'Color','b');
text(300-9,CMPVTH-3.2,'三 一','FontSize',20,'Color','g');
text(360-9,CMPVTH-3.2,'一 五','FontSize',20,'Color','r');

text(60-12-30,CMPVTH2-2.5,'CMPD','FontSize',20,'Color','b');
text(120-12-30,CMPVTH2-2.5,'CMPC','FontSize',20,'Color','g');
text(180-12-30,CMPVTH2-2.5,'CMPB','FontSize',20,'Color','r');
text(240-12-30,CMPVTH2-2.5,'CMPD','FontSize',20,'Color','b');
text(300-12-30,CMPVTH2-2.5,'CMPC','FontSize',20,'Color','g');
text(360-12-30,CMPVTH2-2.5,'CMPB','FontSize',20,'Color','r');

text(60-9-30,CMPVTH2-3.2,'五 四','FontSize',20,'Color','b');
text(120-9-30,CMPVTH2-3.2,'四 六','FontSize',20,'Color','g');
text(180-9-30,CMPVTH2-3.2,'六 二','FontSize',20,'Color','r');
text(240-9-30,CMPVTH2-3.2,'二 三','FontSize',20,'Color','b');
text(300-9-30,CMPVTH2-3.2,'三 一','FontSize',20,'Color','g');
text(360-9-30,CMPVTH2-3.2,'一 五','FontSize',20,'Color','r');

zero_crossing = 0:60:720;
plot(zero_crossing,CMPVTH,'ro','LineWidth',7)

zero_crossing = 30:60:720;
plot(zero_crossing,CMPVTH2,'ro','LineWidth',7)

axis([0 420 0.3 HA_base+2])
xtk=0:60:600;   % 更改後的刻度
set(gca,'xtick',xtk);	%這樣，刻度就會變成0 60 120 180 240、、、

%把y軸刻度清除：
ytk_label={' ',' ',' '};
set(gca,'yticklabel',ytk_label);

%{
for i=1:1:720
    if (mod(i,120) <= 60)
    	ideal(i)=1;
    elseif (mod(i,12) <= 120)
    	ideal(i)=0;
    else
    	ideal(i)=3;
    end
end
ideal(1) = 0;
ideal = ideal + ideal_base;
plot(t,ideal,'r-','LineWidth',5);
text(3,ideal_base+0.5,'五 101','Color','r');
text(63,ideal_base+0.5,'四 100','Color','r');
text(123,ideal_base+0.5,'六 110','Color','r');
text(183,ideal_base+0.5,'二 010','Color','r');
text(243,ideal_base+0.5,'三 011','Color','r');
text(303,ideal_base+0.5,'一 001','Color','r');

for i=1:1:720
    if (mod(i,120) <= 60)
    	real(i)=1;
    elseif (mod(i,12) <= 120)
    	real(i)=0;
    else
    	real(i)=3;
    end
end
real(1) = 0;
real(55) = 0;real(56) = 0;real(57) = 0;
real(60) = 1;real(61) = 1;real(62) = 1;real(63) = 1;

for i=150:1:152
    real(i)=0;
end

for i=180:1:230
    real(i)=1;
end
for i=231:1:250
    real(i)=0;
end

for i=291:1:295
    real(i)=0;
end

for i=305:1:310
    real(i)=1;
end

real = real + real_base;
plot(t,real,'b-','LineWidth',5);

text(50,real_base-0.5,'提早  延遲','Color','b');
text(115,real_base-0.5,'正常','Color','b');
text(147,real_base-0.5,'雜訊','Color','b');
text(175,real_base-0.5,'缺相','Color','b');
text(227,real_base-0.5,'提早         延遲','Color','b');
text(295,real_base-0.5,'雜訊','Color','b');
text(355,real_base-0.5,'正常','Color','b');
%}

%hold off;







