[y, fs]=audioread('welcome.wav');
p=audioplayer(y, fs);
p.SampleRate=1.0*fs; playblocking(p);	% ���� 1.0 ���t�ת����T
p.SampleRate=0.9*fs; playblocking(p);	% ���� 0.9 ���t�ת����T
p.SampleRate=0.8*fs; playblocking(p);	% ���� 0.8 ���t�ת����T
p.SampleRate=0.6*fs; playblocking(p);	% ���� 0.6 ���t�ת����T
