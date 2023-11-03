function [x,fval,iter,exitflag]=Newtons(fun,x0,eps,maxiter)
%NEWTONS   牛頓法求非線性方程式群組的根
% X=NEWTONS(FUN,X0)  牛頓法求非線性方程式群組的解，起始迭代點為X0
% X=NEWTONS(FUN,X0,EPS)  牛頓法求非線性方程式群組的解，精度要求為EPS
% X=NEWTONS(FUN,X0,EPS,MAXITER)  牛頓法求非線性方程式群組的解，最大迭代次數為MAXITER
% [X,FVAL]=NEWTONS(...)  牛頓法求非線性方程式群組的解並傳回解處的函數值
% [X,FVAL,ITER]=NEWTONS(...)  牛頓法求非線性方程式群組的解並傳回迭代次數
% [X,FVAL,ITER,EXITFLAG]=NEWTONS(...)  牛頓法求非線性方程式群組的解並傳回迭代成功標志
%
% 輸導入參數數：
%     ---FUN：非線性方程式群組的符號表達式
%     ---X0：起始迭代點向量
%     ---EPS：精度要求，預設值為1e-6
%     ---MAXITER：最大迭代次數，預設值為1e4
% 輸出參數：
%     ---X：非線性方程式的近似解向量
%     ---FVAL：解處的函數值
%     ---ITER：迭代次數
%     ---EXITFLAG：迭代成功標志，1表示成功，0表示失敗
%
% See also newton

if nargin<2
    error('輸導入參數數至少需要2個.')
end
if nargin<3
    eps=1e-6;
end
if nargin<4
    maxiter=1e4;
end
if isa(fun,'inline')
    fun=char(fun);
    k=strfind(fun,'.');
    fun(k)=[];
    fun=sym(fun);
elseif ~isa(fun,'sym')
    error('函數型態必須是內聯函數或符號函數.')
end
s=symvar(fun);
if length(s)>length(x0)
    error('函數的自由變數過多.')
end
x0=x0(:);
J=jacobian(fun,s);
k=0;err=1;
exitflag=1;
while err>eps
    k=k+1;
    fx0=subs(fun,num2cell(s),num2cell(x0));
    J0=subs(J,num2cell(s),num2cell(x0));
    x1=x0-J0\fx0;
    err=norm(x1-x0);
    x0=x1;
    if k>=maxiter
        exitflag=0;
        break
    end
end
x=x1;
fval=fx0;
iter=k;