duration=3;		% �����ɶ�
recObj=audiorecorder;
fprintf('�����N���}�l %g ������G', duration); pause
fprintf('������...');
recordblocking(recObj, duration);
fprintf('��������\n');
fprintf('�����N���}�l����G'); pause
play(recObj);