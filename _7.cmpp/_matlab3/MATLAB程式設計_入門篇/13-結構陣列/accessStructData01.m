clear student		% �M�� student �ܼ�
student(1) = struct('name', 'Banny', 'scores', [85,80,92,78]);
student(2) = struct('name', 'Joey', 'scores', [80,85,90,88]);
student(3) = struct('name', 'Betty', 'scores', [88,82,90,80]);
student(2).name='Alex';		% ���ܲĤG��ǥͪ��m�W
disp(student(2));			% ��ܲĤG��ǥͪ����
student(3).scores(2)=100;	% ���ܲĤT��ǥͪ��ĤG���p�Ҧ��Z
disp(student(3));			% ��ܲĤT��ǥͪ����
