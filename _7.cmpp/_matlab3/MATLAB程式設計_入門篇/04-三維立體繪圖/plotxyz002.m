z = [0 2 1; 3 2 4; 4 4 4; 7 6 8];
mesh(z);
xlabel('X �b = column index');	% X �b��������r
ylabel('Y �b = row index');	% Y �b��������r

for i=1:size(z,1)
	for j=1:size(z,2)
		h=text(j, i, z(i,j), num2str(z(i, j)));		% �Хܦ�������
		set(h, 'hori', 'center', 'vertical', 'bottom', 'color', 'r');	% ���ܦ�m���C��
	end
end

%colormap(zeros(1,3));		% �H�¦�e�{