[y, fs]=wavread('welcome.wav');
wavplay(y, 1.0*fs, 'sync');	% �P�B���� 1.0 ���t�ת����T
wavplay(y, 0.8*fs, 'async');	% �D�P�B���� 0.8 ���t�ת����T
wavplay(y, 0.6*fs, 'async');	% �D�P�B���� 0.6 ���t�ת����T