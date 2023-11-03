function out = piFun(n)
% piFun: Use sum of sequence to approximate pi

%	Roger Jang, 20030726

total=0;
for i=1:n
	item = (-1)^(i+1)/(2*i-1);
	total = total+item;
end
out = 4*total;