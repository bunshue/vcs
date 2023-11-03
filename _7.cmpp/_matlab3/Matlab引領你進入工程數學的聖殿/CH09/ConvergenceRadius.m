function [R,D]=ConvergenceRadius(an)
%CONVERGENCERADIUS   经计Μ滥畖籔Μ滥办
% R=CONVERGENCERADIUS(AN)  ―经计ANΜ滥畖
% [R,D]=CONVERGENCERADIUS(AN)  ―经计ANΜ滥畖㎝Μ滥办
%
% 块旧把计计
%     ---AN经计兜
% 块把计
%     ---RΜ滥畖
%     ---DΜ滥办
%
% See also limit

n=sym('n','positive');
s=symvar(an);
if ~ismember(n,s)
    error('经计╰计才腹跑计ゲ斗n.')
end
aN=subs(an,n,n+1);
rho=limit(simple(abs(aN/an)),n,inf);
R=1/rho;
if R==0
    D=0;
elseif isinf(double(R))
    D='(-≯,+≯)';
else
    D=[-R,R];
end