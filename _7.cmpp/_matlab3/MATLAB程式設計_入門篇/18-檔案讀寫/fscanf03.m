fid = fopen('test.txt', 'r');
myData = fscanf(fid, '%g', [3, 2]);
fclose(fid);
myData		% ��� myData