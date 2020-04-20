[y, fs]=audioread('welcome.wav');
p=audioplayer(y, fs);
p.SampleRate=1.0*fs; playblocking(p);	% 播放 1.0 倍速度的音訊
p.SampleRate=1.2*fs; playblocking(p);	% 播放 1.2 倍速度的音訊
p.SampleRate=1.5*fs; playblocking(p);	% 播放 1.5 倍速度的音訊
p.SampleRate=2.0*fs; playblocking(p);	% 播放 2.0 倍速度的音訊
