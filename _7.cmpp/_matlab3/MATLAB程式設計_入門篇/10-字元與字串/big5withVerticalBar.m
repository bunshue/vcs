% ��X�]�t "|" ���j���X����r
% Roger Jang, 20040425

range=hex2dec('a440'):hex2dec('c67e');
offendingChar='|';
k=0;
for i=1:length(range)
	numRep=i-1+range(1);
%	fprintf('%d/%d ===> %s\n', i, length(range), char(numRep));
	strRep=dec2hex(numRep);
	if hex2dec(strRep(1:2))==abs(offendingChar) | hex2dec(strRep(3:4))==abs(offendingChar)
		k=k+1;
		%fprintf('"%s" = "%s" + "%s"\n', char(numRep), char(hex2dec(strRep(1:2))), char(hex2dec(strRep(3:4))));
		fprintf('%d. %s\n', k, char(numRep));
	end
end
fprintf('�j���X�`�Φr���A�@�� %d �Ӧr�|�]�t�u%s�v�����X�I\n', k, offendingChar);