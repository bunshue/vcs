fid = fopen('mean.m', 'r');
while feof(fid)==0		% feof �����ɮ׫��ЬO�_�w��F������m
	line = fgetl(fid);
	disp(line);
end