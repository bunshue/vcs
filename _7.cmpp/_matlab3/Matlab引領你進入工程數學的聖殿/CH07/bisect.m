function [x,fx,iter,X]=bisect(fun,a,b,eps,varargin)
%BISECT   二分法求方程式的根
% X=BISECT(FUN,A,B)
% X=BISECT(FUN,A,B,EPS)
% X=BISECT(FUN,A,B,EPS,P1,P2,...)
% [X,FX]=BISECT(...)
% [X,FX,ITER]=BISECT(...)
% [X,FX,ITER,XS]=BISECT(...)
%
% 輸導入參數數：
%     ---FUN：方程式的函數描述，可以為匿名函數、內聯函數或M檔案形式
%     ---A,B：區間端點
%     ---EPS：精度設定
%     ---P1,P2,...：方程式的附加參數
% 輸出參數：
%     ---X：傳回的方程式的根
%     ---FX：方程式根對應的函數值
%     ---ITER：迭代次數
%     ---XS：迭代根序列
%
% See also fzero, RootInterval

if nargin<3
    error('輸導入參數數至少需要3個！')
end
if nargin<4 || isempty(eps)
    eps=1e-6;
end
fa=feval(fun,a,varargin{:});
fb=feval(fun,b,varargin{:});
% fa=fun(a,varargin{:});fb=fun(b,varargin{:});
k=1;
if fa*fb>0  % 不滿足二分法使用條件
    warning(['區間[',num2str(a),',',num2str(b),']內可能沒有根']);
elseif fa==0  % 區間左端點為根
    x=a; fx=fa;
elseif fb==0  % 區間右端點為根
    x=b; fx=fb;
else
    while abs(b-a)>eps;  % 控制二分法結束條件
        x=(a+b)/2;  % 二分區間端點
        fx=feval(fun,x,varargin{:}); % 計算中點的函數值
        if fa*fx>0;  % 條件
            a=x;   % 端點更新
            fa=fx;  % 端點函數值更新
        elseif fb*fx>0;  % 條件
            b=x;  % 端點更新
            fb=fx;  % 端點函數值更新
        else
            break
        end
        X(k)=x;
        k=k+1;
    end
end
iter=k;