encoding='UTF-8';
fid = fopen('chinese_utf8.txt', 'r', 'n', encoding);	
line = fgetl(fid);		% Ū���@�C�ɮפ��e�æL�X  
fclose(fid);
disp(line)

filewrite({line}, 'test.txt');
