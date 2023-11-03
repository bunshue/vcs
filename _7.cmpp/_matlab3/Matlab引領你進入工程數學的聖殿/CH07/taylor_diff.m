function T=taylor_diff(fx,n,x,x0)
%TAYLOR_DIFF   根據泰勒公式的定義式求函數的泰勒展開式
% T=TAYLOR_DIFF(F)
% T=TAYLOR_DIFF(F,N)
% T=TAYLOR_DIFF(F,N,X)
% T=TAYLOR_DIFF(F,N,X,X0)
%
% 輸導入參數數：
%     ---F：函數的符號表達式
%     ---N：泰勒展開式的階次
%     ---X：符號自變數
%     ---X0：泰勒展開點
% 輸出參數：
%     ---T：傳回的泰勒展開式
%
% See also diff, limit

if nargin<4
    x0=0;
end
if nargin<3
    x=symvar(fx);
    if length(x)>1
        error('The Symbolic variable not point out.')
    end
end
if nargin<2
    n=6;
end
a=cell(1,n);
T=limit(fx,x,x0);
for k=2:n
    a{k}=1/sym(factorial(k-1))*limit(diff(fx,x,k-1),x,x0);
    T=T+a{k}*(x-x0)^(k-1);
end
