duration=3;		% 錄音時間
recObj=audiorecorder;
fprintf('按任意鍵後開始 %g 秒錄音：', duration); pause
fprintf('錄音中...');
recordblocking(recObj, duration);
fprintf('錄音結束\n');
fprintf('按任意鍵後開始播放：'); pause
play(recObj);