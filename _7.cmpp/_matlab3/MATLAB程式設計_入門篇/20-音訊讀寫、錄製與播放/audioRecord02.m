fs=16000;	% �����W�v
nBits=16;	% �����I�ѪR�סA�����O 8 �� 16 �� 24
nChannel=1;	% �n�D�ӼơA�����O 1�]���n�D�^ �� 2�]���n�D�Υ��魵�^
duration=3;	% �����ɶ��]��^
recObj=audiorecorder(fs, nBits, nChannel);
fprintf('�����N���}�l %g ������G', duration); pause
fprintf('������...');
recordblocking(recObj, duration);
fprintf('��������\n');
fprintf('�����N���}�l����G'); pause
play(recObj);
y = getaudiodata(recObj, 'double');	% get data as a double array
plot((1:length(data))/fs, y);
xlabel('Time (sec)'); ylabel('Amplitude');