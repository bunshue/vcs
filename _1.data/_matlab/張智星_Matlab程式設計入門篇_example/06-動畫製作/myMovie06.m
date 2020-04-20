x = 0:0.1:8*pi;
k = 0;
h = plot(x, cos(x+k).*cos(x+k).*exp(-x/5), 'EraseMode', 'xor');
axis([-inf inf -1 1]);			% 設定圖軸的範圍
grid on					% 畫出格線
for k = 1:0.01:50
	y = cos(x+k).*cos(x+k).*exp(-x/5);
	set(h, 'ydata', y);		% 設定新的 y 座標
	drawnow				% 立即作圖
end