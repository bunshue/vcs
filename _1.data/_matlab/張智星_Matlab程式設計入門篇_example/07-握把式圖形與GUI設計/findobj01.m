plot(rand(10, 2));		% 畫出兩條曲線  
h=findobj(0, 'type', 'line')	% 找出曲線的握把 
set(h, 'LineWidth', 3);			% 經由握把將曲線寬度改為 3