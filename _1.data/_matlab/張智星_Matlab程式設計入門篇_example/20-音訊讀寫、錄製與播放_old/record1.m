fs=11025;					% �����W�v
duration=2;					% �����ɶ�
fileName='mywelcome.wav';	% ���T�ɮצW��

fprintf('�����N���}�l %g ������G', duration);
pause
fprintf('������...');
y=wavrecord(duration*fs, fs, 'uint8');
fprintf('��������\n');

plot((1:length(y))/fs, y);
z=double(y);
figure;
plot((1:length(y))/fs, (z-mean(z))/128);

fprintf('�����N���}�l����G');
pause
wavplay(y,fs);