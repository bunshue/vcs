function out = isbig5(str)
% isbig5: 測試字串是否為大五碼常用字

%	Roger Jang, 20030518

% 假設送進來的字串已經經過了 xlate 的處理
out = (hex2dec('a440') <= str) & (str <= hex2dec('c67e'));