fs=16000;	% 取樣頻率
nBits=16;	% 取樣點解析度，必須是 8 或 16 或 24
nChannel=1;	% 聲道個數，必須是 1（單聲道） 或 2（雙聲道或立體音）
duration=3;	% 錄音時間（秒）
recObj=audiorecorder(fs, nBits, nChannel);
fprintf('按任意鍵後開始 %g 秒錄音：', duration); pause
fprintf('錄音中...');
recordblocking(recObj, duration);
fprintf('錄音結束\n');
fprintf('按任意鍵後開始播放：'); pause
play(recObj);
y = getaudiodata(recObj, 'double');	% get data as a double array
plot((1:length(y))/fs, y);
xlabel('Time (sec)'); ylabel('Amplitude');