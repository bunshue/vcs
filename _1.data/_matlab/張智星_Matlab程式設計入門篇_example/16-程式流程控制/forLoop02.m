h = zeros(6);	% �ܼ� x �O�@�� 6��6 �j�p���s�x�}
for i = 1:6
	for j = 1:6
		h(i,j) = 1/(i+j-1);
	end
end
format rat		% �ϥΤ��ƧΦ����㦡�Ҧ��ƭ�
h			% ��� h