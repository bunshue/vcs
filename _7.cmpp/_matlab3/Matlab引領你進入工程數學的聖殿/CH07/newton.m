function [x,fx,iter,X]=newton(fun,x0,eps,maxiter)
%NEWTON   箉猭―よ祘Α
% X=NEWTON(FUN,X0)  箉猭―よ祘Α癬﹍翴X0矪
% X=NEWTON(FUN,X0,EPS)  箉猭―よ祘Α癬﹍翴X0矪弘EPS
% X=NEWTON(FUN,X0,EPS,MAXITER)  箉猭―よ祘Α砞﹚程Ω计
% [X,FX]=NEWTON(...)  箉猭―肚矪ㄧ计
% [X,FX,ITER]=NEWTON(...)  箉猭―肚矪ㄧ计のΩ计
% [X,FX,ITER,XS]=NEWTON(...)  箉猭―肚矪ㄧ计Ω计の
%
% 块旧把计计
%     ---FUNよ祘Αㄧ计磞瓃拔ㄧ计ず羛ㄧ计┪M郎Α
%     ---X0癬﹍翴
%     ---EPS弘砞﹚
%     ---MAXITER程Ω计
% 块把计
%     ---X肚よ祘Α
%     ---FXよ祘Α癸莱ㄧ计
%     ---ITERΩ计
%     ---XS
%
% See also fzero, RootInterval, bisect

if nargin<2
    error('块旧把计计ぶ惠璶2')
end
if nargin<3 || isempty(eps)
    eps=1e-6;
end
if nargin<4 || isempty(maxiter)
    maxiter=1e4;
end
s=symvar(fun);
if length(s)>1
    error('ㄧ计funゲ斗珹才腹跑计.')
end
df=diff(fun,s);
k=0;err=1;
while abs(err)>eps
    k=k+1;
    fx0=subs(fun,s,x0);
    dfx0=subs(df,s,x0);
    if dfx0==0
        error('f(x)x0矪旧计0氨ゎ璸衡')
    end
    x1=x0-fx0/dfx0;
    err=x1-x0;
    x0=x1;
    X(k)=x1;
end
if k>=maxiter
    error('Ω计禬ア毖')
end
x=x1;fx=subs(fun,x);iter=k;X=X';