[y, fs]=audioread('welcome.wav');
p=audioplayer(y, fs); playblocking(p);		% 播放正常的音訊波形
p=audioplayer(-y, fs); playblocking(p);		% 播放上下顛倒的音訊波形
p=audioplayer(flipud(y), fs); playblocking(p);	% 播放前後顛倒的音訊波形