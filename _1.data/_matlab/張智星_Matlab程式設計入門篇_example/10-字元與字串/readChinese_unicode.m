encoding='unicode';
fid = fopen('chinese_unicode.txt', 'r', 'n', encoding);	
line = fgetl(fid);		% Ū���@�C�ɮפ��e�æL�X  
fclose(fid);
disp(line)

filewrite({line}, 'test.txt');
