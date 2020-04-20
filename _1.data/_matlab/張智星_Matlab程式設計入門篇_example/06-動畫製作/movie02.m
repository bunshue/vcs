clear M				% �M���q�v��Ưx�} M
r=linspace(0, 4, 30);		% ��L���b�|
t=linspace(0, 2*pi, 50);	% ��L�����y�Ш���
[rr, tt]=meshgrid(r, t);
xx=rr.*cos(tt);			% ���Ͷ�L�W�� x �y��
yy=rr.*sin(tt);			% ���Ͷ�L�W�� y �y��
zz=peaks(xx,yy);		% ���� peaks �b���y�Ъ����
n = 30;				% ��� 30 �ӵe��
scale = cos(linspace(0, 2*pi, n));
figure('Renderer','zbuffer');	% Only used in MS Windows
fprintf('����e����...\n');
for i = 1:n
	surf(xx, yy, zz*scale(i));		% �e��
	axis([-inf inf -inf inf -8.5 8.5]);	% �T�w�϶b���d��
	box on
	M(i) = getframe;			% ����e���A�æs�J�q�v��Ưx�} M  
end
fprintf('����q�v��...\n');
movie(M, 5);					% ����q�v 5 ��