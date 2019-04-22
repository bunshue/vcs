clear,clf

t=0:0.001:3;
%x = sin(10000*t);
for(i=1:1:3000)
    if(i<1500)
        x(i) = 0;
    else
        x(i) = 1;
    end
end

y = fft(x,512);

figure(1);plot(x,'r');hold on;

figure(2);plot(y,'g')

figure(3);plot(abs(y),'g')


