clc;close all;clear all;
%--------------------------義國正轉(HA先遇到HC) = ST之正轉--------------------------
t=1:1:6000;
n=length(t);
for i=1:n
    if (mod(i,360)<=60)
        U(i)=0;
        V(i)=-0.98;
        W(i)=1.02;
        U2(i)=0;
        V2(i)=-0.98;
        W2(i)=1.02*1.4*sind(i*3);
    elseif (mod(i,360)<=120)
        U(i)=-0.98;
        V(i)=0;
        W(i)=1.02;
        U2(i)=-0.98;
        V2(i)=0;
        W2(i)=1.02*1.4*sind((i-60)*3);
    elseif (mod(i,360)<=180)
        U(i)=-0.98;
        V(i)=1.02;
        W(i)=0;
        U2(i)=-0.98;
        V2(i)=1.02*1.4*sind((i-120)*3);
        W2(i)=0;
    elseif (mod(i,360)<=240)
        U(i)=0;
        V(i)=1.02;
        W(i)=-0.98;
        U2(i)=0;
        V2(i)=1.02*1.4*sind((i-180)*3);
        W2(i)=-0.98;
    elseif (mod(i,360)<=300)
        U(i)=1.02;
        V(i)=0;
        W(i)=-0.98;
        U2(i)=1.02*1.4*sind((i-240)*3);
        V2(i)=0;
        W2(i)=-0.98;
    else
        U(i)=1.02;
        V(i)=-0.98;
        W(i)=0;
        U2(i)=1.02*1.4*sind((i-300)*3);
        V2(i)=-0.98;
        W2(i)=0;
    end
end

figure(1);
xtk=0:60:840;   % 更改後的刻度
ytk_label={' ',' ',' '};

U(1)=1.02;
subplot(611);plot(t,U,'r','linewidth',3);axis([0 480 -1.2 1.2]);ylabel('U');set(gca,'xtick',xtk);set(gca,'yticklabel',ytk_label);
V(1)=0;
subplot(612);plot(t,V,'g','linewidth',3);axis([0 480 -1.2 1.2]);ylabel('V');set(gca,'xtick',xtk);set(gca,'yticklabel',ytk_label);
W(1)=0;
subplot(613);plot(t,W,'b','linewidth',3);axis([0 480 -1.2 1.2]);ylabel('W');set(gca,'xtick',xtk);set(gca,'yticklabel',ytk_label);
subplot(614);plot(t,U2,'r','linewidth',3);axis([0 480 -1.2 2.2]);ylabel('U');set(gca,'xtick',xtk);set(gca,'yticklabel',ytk_label);
subplot(615);plot(t,V2,'g','linewidth',3);axis([0 480 -1.2 2.2]);ylabel('V');set(gca,'xtick',xtk);set(gca,'yticklabel',ytk_label);
subplot(616);plot(t,W2,'b','linewidth',3);axis([0 480 -1.2 2.2]);ylabel('W');set(gca,'xtick',xtk);set(gca,'yticklabel',ytk_label);

