clear M				% �M���q�v��Ưx�} M
load clown.mat
image(X); colormap(map);	% �e�X�p���y
n = 30;				% ��� 30 �ӵe��
scale = cos(linspace(0, 2*pi, n));
fprintf('����e����...\n');
for i = 1:n
	colormap(((i-1)*(1-map)+(n-i)*map)/(n-1));	% ���ܦ�L�x�}
	M(i) = getframe;			% ����e���A�æs�J�q�v��Ưx�} M  
end
fprintf('����q�v��...\n');
movie(M, -5);					% ����q�v 5 ��