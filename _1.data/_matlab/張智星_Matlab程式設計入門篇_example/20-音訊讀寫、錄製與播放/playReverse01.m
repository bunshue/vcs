[y, fs]=audioread('welcome.wav');
p=audioplayer(y, fs); playblocking(p);		% ���񥿱`�����T�i��
p=audioplayer(-y, fs); playblocking(p);		% ����W�U�A�˪����T�i��
p=audioplayer(flipud(y), fs); playblocking(p);	% ����e���A�˪����T�i��