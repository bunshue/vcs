[y, fs]=audioread('welcome.wav', [1, inf], 'native');
p=audioplayer(y, fs); play(p);	% 播放此音訊
time=(1:length(y))/fs;	% 時間軸的向量
plot(time, y);	% 畫出時間軸上的波形
class(y)	% 顯示 y 的資料型態