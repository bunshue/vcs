t = 0:0.4:4*pi;
y = sin(t).*exp(-t/5);
fill(t, y, 'y');			% 'y' ������
hold on				% �O�d�¹ϧ�
stem(t, y, 'b');		% �|�W�Ŧ�w�Y��
hold off