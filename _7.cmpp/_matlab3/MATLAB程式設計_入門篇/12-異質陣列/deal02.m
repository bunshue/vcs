dirInfo = dir(matlabroot);			% �C�X MATLAB ���ڥؿ����U�ظ�T
n = length(dirInfo);				% �ɮפΥؿ����Ӽ�
[fileAndDir{1:n}] = deal(dirInfo.name);		% fileAndDir �]�t�U�ɮפΥؿ��W��
dirs = fileAndDir([dirInfo.isdir])		% dirs �]�t�U�ؿ��W��