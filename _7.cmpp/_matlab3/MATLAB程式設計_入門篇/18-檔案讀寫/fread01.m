fid = fopen('test2.txt', 'r');
myData = fread(fid);
char(myData')		% ���ҩ�Ū�J����ƬO�_���T
fclose(fid);