[y, fs]=audioread('welcome.wav');
p=audioplayer(y, fs);
playblocking(p);	% �P�B���� 1.0 ���t�ת����T
sound(y, 0.8*fs);	% �D�P�B���� 0.8 ���t�ת����T
sound(y, 0.6*fs);	% �D�P�B���� 0.6 ���t�ת����T