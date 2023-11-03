[y, fs]=audioread('welcome.wav');	% 載入音訊
sound(5*y, fs);		% 播放音訊
load handel.mat		% 載入音訊
sound(y, Fs);		% 播放音訊
