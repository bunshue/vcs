encoding='Big5';
fid = fopen('chinese_big5.txt', 'r', 'n', encoding);	
line = fgetl(fid);		% Ū���@�C�ɮפ��e�æL�X  
fclose(fid);
disp(line)

filewrite({line}, 'test.txt');
