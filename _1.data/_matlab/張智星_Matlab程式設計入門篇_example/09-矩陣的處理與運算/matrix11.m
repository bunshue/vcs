x1 = rand(10000, 1);
x2 = randn(10000, 1);
subplot(2,1,1); hist(x1, 40); title('���ä��G');
subplot(2,1,2); hist(x2, 40); title('�������G');
set(findobj(gcf, 'type', 'patch'), 'EdgeColor', 'w');	% ����u���զ�
