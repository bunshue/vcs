clear M					% �M���q�v��Ưx�} M
n = 50;					% ��� 50 �ӵe��
figure('Renderer','zbuffer');		% Only used in MS Windows
peaks;
fprintf('����e����...\n');
for i = 1:n
	view([-37.5+i*360/n, 30]);	% �����[������
	M(i) = getframe;		% ����e���A�æs�J�q�v��Ưx�} M  
end
fprintf('����q�v��...\n');
movie(M, 3);				% ����q�v�T��