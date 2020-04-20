[y, fs]=audioread('welcome.wav');
p=audioplayer(y, fs);
p.SampleRate=1.0*fs; playblocking(p);	% 播放 1.0 倍速度的音訊
p.SampleRate=0.9*fs; playblocking(p);	% 播放 0.9 倍速度的音訊
p.SampleRate=0.8*fs; playblocking(p);	% 播放 0.8 倍速度的音訊
p.SampleRate=0.6*fs; playblocking(p);	% 播放 0.6 倍速度的音訊
