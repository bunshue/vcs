fid = fopen('big5.txt');
line = fgetl(fid);		% Ū���@�C�ɮפ��e
fclose(fid);
line2 = xlate(line)		% �ϥ� xlate �N�Q��}������r���X�b�@�_
leng = length(line2)		% ��ܦr�����