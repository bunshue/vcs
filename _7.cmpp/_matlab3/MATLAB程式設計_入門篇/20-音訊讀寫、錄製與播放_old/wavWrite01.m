fs=11025;		% �����W�v
duration=2;		% �����ɶ�
waveFile='test.wav';	% ���x�s�� wav �ɮ�
fprintf('�����N���}�l %g ������G', duration); pause
fprintf('������...');
y=wavrecord(duration*fs, fs);
fprintf('��������\n');
fprintf('�����N���}�l�x�s���T�� %s �ɮ�...', waveFile); pause
nbits=8;			% �C�I���ѪR�׬� 8-bit
wavwrite(y, fs, nbits, waveFile);
fprintf('�s�ɵ���\n');
fprintf('�����N���}�l���� %s...\n', waveFile);
dos(['start ', waveFile]);	% �}�һP wav �ɮ׹��������ε{��