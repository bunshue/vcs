function y=realfunvalue(fun,x)
%REALFUNVALUE   確计絛瞅ず―ㄧ计琘翴矪龟ㄧ计
% Y=REALFUNVALUE(FUN,X)  確计絛瞅ず―ㄧ计FUNX矪龟ㄧ计
%
% 块旧把计计
%     ---FUNㄧ计才腹笷Α
%     ---X疭跑计
% 块把计
%     ---Y肚龟ㄧ计
%
% See also finverse, solve

warning off all
F=subs(fun,x);
if ~isreal(F)
    t=symvar(fun);
    t=sym(t,'real');
    f=finverse(fun);
    y=solve(f-x,t);
else
    y=F;
end
y=double(y);