x = 0:0.1:4*pi;
subplot(2, 2, 1); plot(x, sin(x));		% �������W���ϧ�
subplot(2, 2, 2); plot(x, cos(x));		% �����k�W���ϧ�    	
subplot(2, 2, 3); plot(x, sin(x).*exp(-x/5));	% �����U���ϧ�
subplot(2, 2, 4); plot(x, x.^2);		% �����k�U���ϧ� 