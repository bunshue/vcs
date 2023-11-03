function h=projection(F,G,limit,type)
%PROJECTION   繪制空間曲線在座標面上的投影
% PROJECTION(F,G)  繪制曲面F和G的交線在xOy面上x□[-2*pi,2*pi]的投影
% PROJECTION(F,G,LIMIT)  繪制曲面F和G的交線在xOy面上x□LIMIT的投影
% PROJECTION(F,G,LIMIT,TYPE)  繪制曲面F和G的交線在指定座標面上的投影
% H=PROJECTION(...)  繪制空間曲線在做表面上的投影並傳回其控制碼
%
% 輸導入參數數：
%     ---F,G：兩個相交的曲面方程式
%     ---LIMIT：自變數範圍
%     ---TYPE：指定座標面的型態
% 輸出參數：
%     ---H：投影圖形的控制碼
%
% See also ezplot

if nargin<4
    type='z';
end
if nargin<3
    limit=[-2*pi,2*pi];
end
s=unique([symvar(F),symvar(G)]);
if ~ismember(type,s)
    error('Illegal options.')
end
x=solve(F,type);
G=subs(G,type,x(1));
hp=ezplot(G,limit);
if nargout>0
    h=hp;
end