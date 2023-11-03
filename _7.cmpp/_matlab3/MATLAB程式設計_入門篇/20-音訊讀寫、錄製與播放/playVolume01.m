[y, fs]=audioread('welcome.wav');
p=audioplayer(1*y, fs); playblocking(p);	% 播放 1 倍震幅的音訊
p=audioplayer(3*y, fs); playblocking(p);	% 播放 3 倍震幅的音訊
p=audioplayer(5*y, fs); playblocking(p);	% 播放 5 倍震幅的音訊