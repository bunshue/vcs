function s=Judgment(f,str)
%JUDGMENT   �P�_��ƪ���թʩΥW�Y��
% S=JUDGMENT(F,STR)
%
% ��ɤJ�ѼƼơG
%     ---F�G���
%     ---STR�G�ʽ諬�A�r�ꤸ�M�}�C
% ��X�ѼơG
%     ---S�G�Ǧ^���ʽ諬�A�r��
%
% See also iscellstr, cellstr

if ~iscellstr(str) || numel(str)~=2
    error('Input argument str is Illegal.')
end
if f<0
    s=str{1};
else
    s=str{2};
end