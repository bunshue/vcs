load handel.mat
audioFile='handel.wav';	% 欲儲存的 wav 檔案
fprintf('Saving to %s...\n', audioFile);
audiowrite(audioFile, y, round(1.5*Fs));
%fprintf('按任意鍵後開始播放 %s...\n', audioFile); pause
system(audioFile);	% 開啟與 wav 檔案對應的應用程式