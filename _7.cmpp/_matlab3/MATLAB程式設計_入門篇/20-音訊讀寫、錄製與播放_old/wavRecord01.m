fs=11025;		% �����W�v
duration=2;		% �����ɶ�
fprintf('�����N���}�l %g ������G', duration); pause
fprintf('������...');
y=wavrecord(duration*fs, fs);	% duration*fs �O��������I��
fprintf('��������\n');
fprintf('�����N���}�l����G'); pause
wavplay(y,fs);