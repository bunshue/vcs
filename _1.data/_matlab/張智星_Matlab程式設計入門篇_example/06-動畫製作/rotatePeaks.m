r=linspace(0, 4, 30);		% 圓盤的半徑
t=linspace(0, 2*pi, 50);	% 圓盤的極座標角度
[rr, tt]=meshgrid(r, t);
xx=rr.*cos(tt);			% 產生圓盤上的 x 座標
yy=rr.*sin(tt);			% 產生圓盤上的 y 座標
zz=peaks(xx, yy);		% 產生 peaks 在極座標的資料
n=300;				% 抓取 30 個畫面
for i=1:n
	rrtt=rr.*exp(sqrt(-1)*(tt+i/20));
	surfl(real(rrtt), imag(rrtt), zz);		% 畫圖
	colormap pink; shading interp
	drawnow;
end