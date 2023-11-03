[y, fs]=audioread('welcome.wav');	% 讀入音訊
p=audioplayer(y, fs);
playblocking(p);	% 播放音訊
load handel.mat		% 載入音訊
p=audioplayer(y, Fs);
playblocking(p);	% 播放音訊