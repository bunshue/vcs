fid = fopen('big5.txt');
line = fgetl(fid);			% Ū���@�C�ɮפ��e
fclose(fid);
line2 = native2unicode(line, 'big5')	% �ϥ� native2unicode �N�Q��}������r���X�b�@�_
leng = length(line2)			% ��ܦr�����