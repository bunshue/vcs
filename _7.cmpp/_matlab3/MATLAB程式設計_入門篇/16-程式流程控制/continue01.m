x = [1 -2 3 -4 5];
posTotal = 0;
for i = 1:length(x)
	if x(i)<0, continue; end	% �Y x(i) �p��s�A�������즹�j�骺�U�@�ӽ��j
	posTotal=posTotal+x(i);
end
posTotal	% ��� posTotal ����