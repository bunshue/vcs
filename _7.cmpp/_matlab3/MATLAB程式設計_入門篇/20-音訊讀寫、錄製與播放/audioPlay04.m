[y, fs]=audioread('welcome.wav');	% Ū�J���T
p=audioplayer(y, fs);
playblocking(p);	% ���񭵰T
load handel.mat		% ���J���T
p=audioplayer(y, Fs);
playblocking(p);	% ���񭵰T