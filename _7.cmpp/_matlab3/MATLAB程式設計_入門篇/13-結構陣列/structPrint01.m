clear student		% �M�� student �ܼ�
student(1) = struct('name', '�i�x��', 'scores', [85, 80]);
student(2) = struct('name', '��ѻT', 'scores', [80, 85]);
student(3) = struct('name', '������', 'scores', [88, 82]);
for i = 1:length(student)	% �C�L�X�C�Ӿǥͪ��W�r  
	fprintf ('student %g: %s\n', i, student(i).name);     
end  