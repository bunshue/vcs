x = 0:0.1:8*pi;
k = 0;
h = plot(x, cos(x+k).*cos(x+k).*exp(-x/5), 'EraseMode', 'xor');
axis([-inf inf -1 1]);			% �]�w�϶b���d��
grid on					% �e�X��u
for k = 1:0.01:50
	y = cos(x+k).*cos(x+k).*exp(-x/5);
	set(h, 'ydata', y);		% �]�w�s�� y �y��
	drawnow				% �ߧY�@��
end