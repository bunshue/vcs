t = 0:0.4:4*pi;
y = cos(t).*exp(-t/5);
stairs(t, y);
hold on				% �O�d�¹ϧ�
stem(t, y);			% �|�W�w�Y��
hold off