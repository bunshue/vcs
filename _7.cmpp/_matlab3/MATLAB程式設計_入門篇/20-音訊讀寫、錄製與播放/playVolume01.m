[y, fs]=audioread('welcome.wav');
p=audioplayer(1*y, fs); playblocking(p);	% ���� 1 ���_�T�����T
p=audioplayer(3*y, fs); playblocking(p);	% ���� 3 ���_�T�����T
p=audioplayer(5*y, fs); playblocking(p);	% ���� 5 ���_�T�����T