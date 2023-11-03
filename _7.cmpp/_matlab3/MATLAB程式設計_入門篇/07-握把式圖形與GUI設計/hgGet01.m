t=0:0.4:4*pi;
h=plot(t, exp(-t/5).*sin(t));			% h 為曲線的握把
set(h, 'Marker', 'diamond', 'MarkerSize', 15, 'MarkerFaceColor', 'r');	% 將線標改成菱形、線標大小改成 15、線標的邊色改成紅色
fprintf('MATLAB version = %s\n', version);
get(h)		% 列出 h 的所有性質