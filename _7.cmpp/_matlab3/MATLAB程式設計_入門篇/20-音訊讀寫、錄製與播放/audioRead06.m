[y, fs]=audioread('welcome.wav', [1, inf], 'native');
p=audioplayer(y, fs); play(p);	% ���񦹭��T
time=(1:length(y))/fs;	% �ɶ��b���V�q
plot(time, y);	% �e�X�ɶ��b�W���i��
class(y)	% ��� y ����ƫ��A