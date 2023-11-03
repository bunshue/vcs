function varargout=SeparableVarsDE(F,G,x,y,varargin)
%SEPARABLEVARSDE   可分離變數方程式的求解
% L=SEPARABLEVARSDE(F,G,X,Y)  求微分方程式G(Y)dY=F(X)dX的通解
% L=SEPARABLEVARSDE(F,G,X,Y,COND)  求微分方程式G(Y)dY=F(X)dX滿足條件COND的特解
%
% 輸導入參數數：
%     ---F,G：關於X和Y的函數
%     ---X,Y：函數F和G的自變數
%     ---COND：初值條件
% 輸出參數：
%     ---L：微分方程式的解
%
% See also int, solve

Iy=int(F,x);
Ix=int(G,y);
syms C real
I=Iy-Ix-C;
if nargin==4
    varargout{1}=[char(I),'=0'];
elseif nargin==5
    cond=varargin{:};
    k1=strfind(cond,'(');
    k2=strfind(cond,')');
    k3=strfind(cond,'=');
    x0=sym(cond(k1(1)+1:k2(1)-1));
    y0=sym(cond(k3+1:end));
    C1=solve(subs(I,{x,y},{x0,y0}),C);
    varargout{1}=[char(subs(I,C,C1)),'=0'];
else
    error('Illegal input arguments.')
end