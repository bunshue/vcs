
filename = 'mono.wav';
[y, fs] = audioread(filename);

figure(1)
%sound(y, fs); % 播放此音訊, fs: sample rate = 11025
time = (1:length(y))/fs; % 時間軸的向量
plot(time, y); % 畫出時間軸上的波形

info=audioinfo(filename);
fprintf('檔案名稱 = %s\n', info.Filename);
fprintf('壓縮方式 = %s\n', info.CompressionMethod);
fprintf('通道個數 = %g 個\n', info.NumChannels);
fprintf('取樣頻率 = %g Hz\n', info.SampleRate);
fprintf('取樣點總個數 = %g 個\n', info.TotalSamples);
fprintf('音訊長度 = %g 秒\n', info.Duration);
fprintf('取樣點解析度 = %g 位元/取樣點\n', info.BitsPerSample);


figure(2)
filename = 'stereo.wav';
[y, fs]=audioread(filename); % 讀取音訊檔
%sound(y, fs); % 播放音訊
left=y(:,1); % 左聲道音訊
right=y(:,2); % 右聲道音訊
time = (1:length(y))/fs; % 時間軸的向量
subplot(3,1,1)
plot(time, y); % 左右聲道畫一起
subplot(3,1,2)
plot((1:length(left))/fs, left);	% 畫左聲道
subplot(3,1,3)
plot((1:length(right))/fs, right);	% 畫右聲道


%讀出部分檔案
figure(3)
filename = 'original_speech.wav';
[y, fs] = audioread(filename, [4001 50000]); % 讀取音訊檔第4001至50000點
plot(y)

%讀出部分檔案, 加入'native'讀出的音訊就會是以原來檔案內的資料型態為準
figure(4)
filename = 'original_speech.wav';
[y, fs] = audioread(filename, [4001 50000], 'native');
plot(y)

