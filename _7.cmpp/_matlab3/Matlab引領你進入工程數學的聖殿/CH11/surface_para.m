function surface_para(funx,funy,funz,varargin)
%SURFACE_PARA   酶把计よ祘ΑボΡ┪把计よ祘ΑボΡ絬露z禸臂锣┮眔臂锣Ρ
% SURFACE_PARA(FUNX,FUNY,FUNZ,T)  酶把计よ祘Α絋﹚Ρ絬露z禸臂锣臂锣Ρ
% SURFACE_PARA(FUNX,FUNY,FUNZ,U,V)  酶把计よ祘Α絋﹚Ρ
%
% 块旧把计计
%     ---FUNX,FUNY,FUNZ把计よ祘Α琌Ρ絬┪Ρ
%     ---TΡ絬把计よ祘Α跑计
%     ---U,VΡ把计よ祘Α跑计
%
% See also surf

s=unique([symvar(funx),symvar(funy),symvar(funz)]);
if length(s)==1
    theta=linspace(0,2*pi);
    t=varargin{1};
    [T,Th]=meshgrid(t,theta);
    X=subs(sqrt(funx^2+funy^2),s,T).*cos(Th);
    Y=subs(sqrt(funx^2+funy^2),s,T).*sin(Th);
    Z=subs(funz,s,T);
elseif length(s)==2
    [u,v]=deal(varargin{:});
    [U,V]=meshgrid(u,v);
    X=subs(funx,num2cell(s),{U,V});
    Y=subs(funy,num2cell(s),{U,V});
    Z=subs(funz,num2cell(s),{U,V});
else
    error('把计よ祘Α把计计Τ粇.')
end
surf(X,Y,Z)