x = 0:0.1:8*pi;
h = plot(x, sin(x).*exp(-x/5), 'EraseMode', 'xor');
axis([-inf inf -1 1]);			% �]�w�϶b���d��
grid on					% �e�X��u
tic
for i = 1:5000
	y = sin(x-i/50).*exp(-x/5);
	set(h, 'ydata', y);		% �]�w�s�� y �y��
	drawnow				% �ߧY�@��
end
toc