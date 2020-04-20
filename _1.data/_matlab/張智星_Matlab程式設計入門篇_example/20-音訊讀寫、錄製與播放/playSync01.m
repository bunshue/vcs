[y, fs]=audioread('welcome.wav');
p=audioplayer(y, fs);
playblocking(p);	% 同步播放 1.0 倍速度的音訊
sound(y, 0.8*fs);	% 非同步播放 0.8 倍速度的音訊
sound(y, 0.6*fs);	% 非同步播放 0.6 倍速度的音訊