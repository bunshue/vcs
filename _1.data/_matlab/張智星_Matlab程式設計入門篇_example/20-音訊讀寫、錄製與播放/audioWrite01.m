load handel.mat
audioFile='handel.wav';	% ���x�s�� wav �ɮ�
fprintf('Saving to %s...\n', audioFile);
audiowrite(audioFile, y, round(1.5*Fs));
%fprintf('�����N���}�l���� %s...\n', audioFile); pause
system(audioFile);	% �}�һP wav �ɮ׹��������ε{��