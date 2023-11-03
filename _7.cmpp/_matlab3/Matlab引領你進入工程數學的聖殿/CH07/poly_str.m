function d=poly_str(xd,yd,xi,N)
%POLY_STR   插值型求導算法
% D=POLY_STR(XD,YD,XI,N)  首先資料XD,YD進行多項式插值並求其在點XI處的N階導數
%
% 輸導入參數數：
%     ---XD,YD：實驗資料
%     ---XI：數值求導點
%     ---N：求導階次
% 輸出參數：
%     ---D：N階數值導數
%
% See also diff, polyfit, polyder, polyval

L=length(xd)-1;
p=polyfit(xd,yd,L);
for k=1:N
    p=polyder(p);
end
d=polyval(p,xi);