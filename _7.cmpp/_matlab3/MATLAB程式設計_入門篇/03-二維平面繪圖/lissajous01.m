
t=linspace(0, 2*pi, 1001);
x=cos(t);
y=sin(2*t);
plot(x,y);


for i=1:5
	for j=1:5
		subplot(5, 5, i+(j-1)*5);
		x=cos(i*t);
		y=sin(j*t);
		plot(x, y); axis image
		title(sprintf('m=%d, n=%d\n', i, j));
	end
end

