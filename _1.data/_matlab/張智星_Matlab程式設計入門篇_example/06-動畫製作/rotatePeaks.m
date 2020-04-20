r=linspace(0, 4, 30);		% ��L���b�|
t=linspace(0, 2*pi, 50);	% ��L�����y�Ш���
[rr, tt]=meshgrid(r, t);
xx=rr.*cos(tt);			% ���Ͷ�L�W�� x �y��
yy=rr.*sin(tt);			% ���Ͷ�L�W�� y �y��
zz=peaks(xx, yy);		% ���� peaks �b���y�Ъ����
n=300;				% ��� 30 �ӵe��
for i=1:n
	rrtt=rr.*exp(sqrt(-1)*(tt+i/20));
	surfl(real(rrtt), imag(rrtt), zz);		% �e��
	colormap pink; shading interp
	drawnow;
end