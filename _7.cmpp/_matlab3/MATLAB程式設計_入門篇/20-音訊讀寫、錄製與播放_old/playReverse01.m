[y, fs]=wavread('welcome.wav');
wavplay(y, fs, 'sync');			% ���񥿱`�����T�i��
wavplay(-y, fs, 'sync');		% ����W�U�A�˪����T�i��
wavplay(flipud(y), fs, 'sync');		% ����e���A�˪����T�i��