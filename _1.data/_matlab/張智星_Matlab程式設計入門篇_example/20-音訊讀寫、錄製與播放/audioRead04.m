fileName='flanger.wav';
[y, fs]=audioread(fileName);	% Ū�����T��
sound(y, fs);	% ���񭵰T
left=y(:,1);	% ���n�D���T
right=y(:,2);	% �k�n�D���T
subplot(2,1,1), plot((1:length(left))/fs, left);
subplot(2,1,2), plot((1:length(right))/fs, right);