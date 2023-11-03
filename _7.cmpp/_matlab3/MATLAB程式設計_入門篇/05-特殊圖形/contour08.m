t = linspace(0, 2*pi, 61);	% 角度的格子點
r = 0:0.05:1;			% 長度的格子點
[tt, rr] = meshgrid(t, r);	% 產生二維的格子點
[xx, yy] = pol2cart(tt, rr);	% 將極座標轉換至直角座標
zz = xx + sqrt(-1)*yy;		% 複數表示，亦可寫成 zz=rr.*exp(sqrt(-1)*tt);
ff = abs(zz.^3-1);		% 曲面的函數
h = polar([0 0], [0 1]);	% 產生在極座標上的一條直線
delete(h);			% 移除上述圖形，但留下極座標圖軸
hold on
contour(xx, yy, ff, 50);	% 畫出等高線
hold off