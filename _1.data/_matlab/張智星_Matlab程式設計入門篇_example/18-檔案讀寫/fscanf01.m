fid = fopen('test.txt', 'r');
myData = fscanf(fid, '%g');
fclose(fid);
myData		% ��� myData