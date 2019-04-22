clc;close all;clear all;
%--------------------------義國正轉(HA先遇到HC) = ST之正轉--------------------------
t=1:1:6000;
n=length(t);
for i=1:n
    if (mod(i,360)<=180)
        A(i)=1.02;
    else
        A(i)=0.02;
    end
end
for i=1:n
    if ((mod(i,360)<=60)||(mod(i,360)>=240))
        B(i)=1;
    else
        B(i)=0;
    end
end
for i=1:n
    if ((mod(i,360)>=120)&&(mod(i,360)<=300))
        C(i)=0.98;
    else
        C(i)=-0.02;
    end
end

for i=1:n
    if (mod(i,360)<=60)
        U(i)=0;
        V(i)=-0.98;
        W(i)=1.02;
    elseif (mod(i,360)<=120)
        U(i)=-0.98;
        V(i)=0;
        W(i)=1.02;
    elseif (mod(i,360)<=180)
        U(i)=-0.98;
        V(i)=1.02;
        W(i)=0;
    elseif (mod(i,360)<=240)
        U(i)=0;
        V(i)=1.02;
        W(i)=-0.98;
    elseif (mod(i,360)<=300)
        U(i)=1.02;
        V(i)=0;
        W(i)=-0.98;
    else
        U(i)=1.02;
        V(i)=-0.98;
        W(i)=0;
    end
end

figure(1);
xtk=0:60:840;   % 更改後的刻度
ytk_label={' ',' ',' '};

subplot(711);axis([0 480 0 1]);ylabel('code');set(gca,'xtick',xtk);set(gca,'yticklabel',ytk_label);title('義國正轉(HA先遇到HC) = ST之正轉');

text(20,0.7,'六 110');
text(80,0.7,'四 100');
text(140,0.7,'五 101');
text(200,0.7,'一 001');
text(260,0.7,'三 011');
text(320,0.7,'二 010');

text(18,0.3,'A:U0V-W+');
text(78,0.3,'B:U-V0W+');
text(138,0.3,'C:U-V+W0');
text(198,0.3,'D:U0V+W-');
text(258,0.3,'E:U+V0W-');
text(318,0.3,'F:U+V-W0');

A(1)=0;subplot(712);plot(t,A,'r','linewidth',3);axis([0 480 -0.2 1.2]);ylabel('HA');set(gca,'xtick',xtk);set(gca,'yticklabel',ytk_label);
subplot(713);plot(t,B,'g','linewidth',3);axis([0 480 -0.2 1.2]);ylabel('HB');set(gca,'xtick',xtk);set(gca,'yticklabel',ytk_label);
subplot(714);plot(t,C,'b','linewidth',3);axis([0 480 -0.2 1.2]);ylabel('HC');set(gca,'xtick',xtk);set(gca,'yticklabel',ytk_label);
U(1)=1.02;
subplot(715);plot(t,U,'r','linewidth',3);axis([0 480 -1.2 1.2]);ylabel('U');set(gca,'xtick',xtk);set(gca,'yticklabel',ytk_label);
V(1)=0;
subplot(716);plot(t,V,'g','linewidth',3);axis([0 480 -1.2 1.2]);ylabel('V');set(gca,'xtick',xtk);set(gca,'yticklabel',ytk_label);
W(1)=0;
subplot(717);plot(t,W,'b','linewidth',3);axis([0 480 -1.2 1.2]);ylabel('W');set(gca,'xtick',xtk);set(gca,'yticklabel',ytk_label);

%--------------------------義國反轉(HA先遇到HB) = ST之反轉--------------------------
t=1:1:6000;
n=length(t);
for i=1:n
    if (mod(i,360)<=180)
        A(i)=1.02;
    else
        A(i)=0.02;
    end
end
for i=1:n
    if ((mod(i,360)<=300)&&(mod(i,360)>=120))
        B(i)=1;
    else
        B(i)=0;
    end
end
for i=1:n
    if ((mod(i,360)<=60)||(mod(i,360)>=240))
        C(i)=0.98;
    else
        C(i)=-0.02;
    end
end

for i=1:n
    if (mod(i,360)<=60)
        V(i)=-1;
        W(i)=0;
        U(i)=1;
    elseif (mod(i,360)<=120)
        V(i)=0;
        W(i)=-1;
        U(i)=1;
    elseif (mod(i,360)<=180)
        V(i)=1;
        W(i)=-1;
        U(i)=0;
    elseif (mod(i,360)<=240)
        V(i)=+1;
        W(i)=0;
        U(i)=-1;
    elseif (mod(i,360)<=300)
        V(i)=0;
        W(i)=1;
        U(i)=-1;
    else
        V(i)=-1;
        W(i)=1;
        U(i)=0;
    end
end

figure(2);
xtk=0:60:840;   % 更改後的刻度
ytk_label={' ',' ',' '};

A(1)=0;subplot(711);axis([0 480 0 1]);ylabel('code');set(gca,'xtick',xtk);set(gca,'yticklabel',ytk_label);title('義國反轉(HA先遇到HB) = ST之反轉');

text(20,0.7,'五 101');
text(80,0.7,'四 100');
text(140,0.7,'六 110');
text(200,0.7,'二 010');
text(260,0.7,'三 011');
text(320,0.7,'一 001');

text(18,0.3,'F:U+V-W0');
text(78,0.3,'E:U+V0W-');
text(138,0.3,'D:U0V+W-');
text(198,0.3,'C:U-V+W0');
text(258,0.3,'B:U-V0W+');
text(318,0.3,'A:U0V-W+');

U(1)=0;V(1)=-1;W(1)=1;

subplot(712);plot(t,A,'r','linewidth',3);axis([0 480 -0.2 1.2]);ylabel('HA');set(gca,'xtick',xtk);set(gca,'yticklabel',ytk_label);
subplot(713);plot(t,B,'g','linewidth',3);axis([0 480 -0.2 1.2]);ylabel('HB');set(gca,'xtick',xtk);set(gca,'yticklabel',ytk_label);
subplot(714);plot(t,C,'b','linewidth',3);axis([0 480 -0.2 1.2]);ylabel('HC');set(gca,'xtick',xtk);set(gca,'yticklabel',ytk_label);
subplot(715);plot(t,U,'r','linewidth',3);axis([0 480 -1.2 1.2]);ylabel('U');set(gca,'xtick',xtk);set(gca,'yticklabel',ytk_label);
subplot(716);plot(t,V,'g','linewidth',3);axis([0 480 -1.2 1.2]);ylabel('V');set(gca,'xtick',xtk);set(gca,'yticklabel',ytk_label);
subplot(717);plot(t,W,'b','linewidth',3);axis([0 480 -1.2 1.2]);ylabel('W');set(gca,'xtick',xtk);set(gca,'yticklabel',ytk_label);

%--------------------------佶慶正轉(HA先遇到HB)--------------------------
t=1:1:6000;
n=length(t);
for i=1:n
    if (mod(i,360)<=180)
        A(i)=1.02;
    else
        A(i)=0.02;
    end
end
for i=1:n
    if ((mod(i,360)<=300)&&(mod(i,360)>=120))
        B(i)=1;
    else
        B(i)=0;
    end
end
for i=1:n
    if ((mod(i,360)<=60)||(mod(i,360)>=240))
        C(i)=0.98;
    else
        C(i)=-0.02;
    end
end

for i=1:n
    if (mod(i,360)<=60)
        U(i)=1.02;
        V(i)=0;
        W(i)=-0.98;
    elseif (mod(i,360)<=120)
        U(i)=0;
        V(i)=1.02;
        W(i)=-0.98;
    elseif (mod(i,360)<=180)
        U(i)=-0.98;
        V(i)=1.02;
        W(i)=0;
    elseif (mod(i,360)<=240)
        U(i)=-0.98;
        V(i)=0;
        W(i)=1.02;
    elseif (mod(i,360)<=300)
        U(i)=0;
        V(i)=-0.98;
        W(i)=1.02;
    else
        U(i)=1.02;
        V(i)=-0.98;
        W(i)=0;
    end
end

figure(3);
xtk=0:60:840;   % 更改後的刻度
ytk_label={' ',' ',' '};

A(1)=0;subplot(711);axis([0 480 0 1]);ylabel('code');set(gca,'xtick',xtk);set(gca,'yticklabel',ytk_label);title('佶慶正轉(HA先遇到HB)');

text(15,0.7,'5 101');
text(75,0.7,'4 100');
text(135,0.7,'6 110');
text(195,0.7,'2 010');
text(255,0.7,'3 011');
text(315,0.7,'1 001');

text(20,0.3,'一');
text(80,0.3,'二');
text(140,0.3,'三');
text(200,0.3,'四');
text(260,0.3,'五');
text(320,0.3,'六');

subplot(712);plot(t,A,'r','linewidth',3);axis([0 480 -0.2 1.2]);ylabel('A');set(gca,'xtick',xtk);set(gca,'yticklabel',ytk_label);
subplot(713);plot(t,B,'g','linewidth',3);axis([0 480 -0.2 1.2]);ylabel('B');set(gca,'xtick',xtk);set(gca,'yticklabel',ytk_label);
subplot(714);plot(t,C,'b','linewidth',3);axis([0 480 -0.2 1.2]);ylabel('C');set(gca,'xtick',xtk);set(gca,'yticklabel',ytk_label);
subplot(715);plot(t,U,'r','linewidth',3);axis([0 480 -1.2 1.2]);ylabel('U');set(gca,'xtick',xtk);set(gca,'yticklabel',ytk_label);
V(1)=-0.98;subplot(716);plot(t,V,'g','linewidth',3);axis([0 480 -1.2 1.2]);ylabel('V');set(gca,'xtick',xtk);set(gca,'yticklabel',ytk_label);
W(1)=0;subplot(717);plot(t,W,'b','linewidth',3);axis([0 480 -1.2 1.2]);ylabel('W');set(gca,'xtick',xtk);set(gca,'yticklabel',ytk_label);

%--------------------------ST反轉(HA先遇到HB)--------------------------
t=1:1:6000;
n=length(t);
for i=1:n
    if (mod(i,360)<=180)
        A(i)=1.02;
    else
        A(i)=0.02;
    end
end
for i=1:n
    if ((mod(i,360)<=300)&&(mod(i,360)>=120))
        B(i)=1;
    else
        B(i)=0;
    end
end
for i=1:n
    if ((mod(i,360)<=60)||(mod(i,360)>=240))
        C(i)=0.98;
    else
        C(i)=-0.02;
    end
end

for i=1:n
    if (mod(i,360)<=60)
        V(i)=-1;
        W(i)=0;
        U(i)=1;
    elseif (mod(i,360)<=120)
        V(i)=0;
        W(i)=-1;
        U(i)=1;
    elseif (mod(i,360)<=180)
        V(i)=1;
        W(i)=-1;
        U(i)=0;
    elseif (mod(i,360)<=240)
        V(i)=+1;
        W(i)=0;
        U(i)=-1;
    elseif (mod(i,360)<=300)
        V(i)=0;
        W(i)=1;
        U(i)=-1;
    else
        V(i)=-1;
        W(i)=1;
        U(i)=0;
    end
end

figure(4);
xtk=0:60:840;   % 更改後的刻度
ytk_label={' ',' ',' '};

A(1)=0;subplot(711);axis([0 480 0 1]);ylabel('code');set(gca,'xtick',xtk);set(gca,'yticklabel',ytk_label);title('ST反轉(HA先遇到HB)');

text(19,0.7,'101');
text(79,0.7,'001');
text(139,0.7,'011');
text(199,0.7,'010');
text(259,0.7,'110');
text(319,0.7,'100');

text(20,0.3,'一');
text(80,0.3,'六');
text(140,0.3,'五');
text(200,0.3,'四');
text(260,0.3,'三');
text(320,0.3,'二');

U(1)=0;V(1)=-1;W(1)=1;

subplot(712);plot(t,A,'r','linewidth',3);axis([0 480 -0.2 1.2]);ylabel('A');set(gca,'xtick',xtk);set(gca,'yticklabel',ytk_label);
subplot(713);plot(t,B,'g','linewidth',3);axis([0 480 -0.2 1.2]);ylabel('B');set(gca,'xtick',xtk);set(gca,'yticklabel',ytk_label);
subplot(714);plot(t,C,'b','linewidth',3);axis([0 480 -0.2 1.2]);ylabel('C');set(gca,'xtick',xtk);set(gca,'yticklabel',ytk_label);
subplot(715);plot(t,U,'r','linewidth',3);axis([0 480 -1.2 1.2]);ylabel('U');set(gca,'xtick',xtk);set(gca,'yticklabel',ytk_label);
subplot(716);plot(t,V,'g','linewidth',3);axis([0 480 -1.2 1.2]);ylabel('V');set(gca,'xtick',xtk);set(gca,'yticklabel',ytk_label);
subplot(717);plot(t,W,'b','linewidth',3);axis([0 480 -1.2 1.2]);ylabel('W');set(gca,'xtick',xtk);set(gca,'yticklabel',ytk_label);


