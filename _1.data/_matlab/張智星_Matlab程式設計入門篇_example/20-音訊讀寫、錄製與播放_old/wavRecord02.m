fs=11025;		% �����W�v
duration=2;		% �����ɶ�
channel=1;		% ���n�D
fprintf('�����N���}�l %g ������G', duration); pause
fprintf('������...');
y=wavrecord(duration*fs, fs, channel, 'uint8');	% duration*fs �O��������I��
fprintf('��������\n');
fprintf('�����N���}�l����G'); pause
wavplay(y,fs);