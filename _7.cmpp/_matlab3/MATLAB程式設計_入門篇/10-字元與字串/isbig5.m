function out = isbig5(str)
% isbig5: ���զr��O�_���j���X�`�Φr

%	Roger Jang, 20030518

% ���]�e�i�Ӫ��r��w�g�g�L�F xlate ���B�z
out = (hex2dec('a440') <= str) & (str <= hex2dec('c67e'));