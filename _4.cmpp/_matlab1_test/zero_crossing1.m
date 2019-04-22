%範例：信號加雜訊
clear,clc,clf
t=1:1:720;
%u=sind(t);
%plot(t,u,'r-');hold on;
%u_n=u+(rand(1,length(t))-0.5)*0.3;
%save u_n_data.dat u_n -ascii

u_n = load('u_n_data.dat')	%叫出來，變成以u_n命名的變數：
plot(t,u_n,'r-');hold on;


u_z(1)= 0;
for i=1:1:719
    if(sign(u_n(i)) ~=sign(u_n(i+1)))
        u_z(i+1) = 1-u_z(i);
    else
        u_z(i+1) = u_z(i);
    end
end
plot(t,u_z,'b-')




