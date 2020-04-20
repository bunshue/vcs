x=linspace(-1, 1)';
y=[];
for m=1:5
	y=[y, cos(m*acos(x))];
end
plot(x, y);
legend('m=1', 'm=2', 'm=3', 'm=4', 'm=5');
axis image