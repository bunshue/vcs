[y, fs]=audioread('welcome.wav');
sound(y, fs);	% ���񦹭��T
time=(1:length(y))/fs;	% �ɶ��b���V�q
plot(time, y);	% �e�X�ɶ��b�W���i��