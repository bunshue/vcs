function x=rsolve(F,G,u,x0)
%RSOLVE   z跑传―秆瞒床絬┦﹚盽╰参
% X=RSOLVE(F,G,U,X0)  ―絬┦﹚盽╰参X(k+1)=F*X(k)+G*U(k)秆
%
% 块旧把计计
%     ---F,G╰参╰计痻皚
%     ---U╰参块
%     ---X0╰参
% 块把计
%     ---X╰参秆
%
% See also ztrans, iztrans

[m,n]=size(F);
[q,p]=size(G);
r=length(u);
if m~=n || n~=q
    error('╰计痻皚蝴计ぃ才.')
end
if isvector(u)
    if r~=p
        error('块秖籔北痻皚蝴计ぃ才.')
    end
end
I=sym(eye(size(F)));
syms z k
U=ztrans(sym(u));
x=simple(iztrans((z*I-sym(F))\(z*sym(x0)+sym(G)*U),z,k));