[y, fs]=audioread('welcome.wav');
p=audioplayer(y, fs);
p.SampleRate=1.0*fs; playblocking(p);	% ���� 1.0 ���t�ת����T
p.SampleRate=1.2*fs; playblocking(p);	% ���� 1.2 ���t�ת����T
p.SampleRate=1.5*fs; playblocking(p);	% ���� 1.5 ���t�ת����T
p.SampleRate=2.0*fs; playblocking(p);	% ���� 2.0 ���t�ת����T
