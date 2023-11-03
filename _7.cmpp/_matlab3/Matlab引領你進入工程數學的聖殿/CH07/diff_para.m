function result=diff_para(y,x,t,n)
%DIFF_PARA   把计よ祘Α―旧
% R=DIFF_PARA(Y,X)┪R=DIFF_PARA(Y,X,[])  讽才腹笷ΑXΤ才腹跑计
%                                                ―パX㎝Y∕﹚把计よ祘Α旧计dY/dX
% R=DIFF_PARA(Y,X,T)  ―パX㎝Y∕﹚把计よ祘Α闽跑计T旧计dY/dX
% R=DIFF_PARA(Y,X,T,N)  ―パX㎝Y∕﹚把计よ祘Α闽跑计TN顶旧计dNY/dXN
%
% 块旧把计计
%     ---Y,X把计よ祘Α才腹笷Α
%     ---T把计よ祘Α才腹跑计
%     ---N―旧顶Ω
% 块把计
%     ---R把计よ祘Α―旧挡狦
%
% See also diff

if nargin<4
    n=1;
end
if nargin==2 || isempty(t)
    t=symvar(x);
    if length(t)>1
        error('The Symbolic variable not point out.')
    end
end
if n==1
    result=diff(y,t)/diff(x,t);
else
    result=diff(diff_para(y,x,t,n-1),t)/diff(x,t);
end
