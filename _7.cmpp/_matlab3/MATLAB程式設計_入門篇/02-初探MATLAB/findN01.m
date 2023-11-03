maxN = 1000;
for n=1:maxN
	value = prod(1:n);
	if value>realmax
		break;
	end
end
fprintf('n = %d\n', n);
fprintf('(n-1)! = %d\n', prod(1:n-1));