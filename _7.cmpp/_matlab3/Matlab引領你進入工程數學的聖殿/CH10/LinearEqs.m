function [x,e]=LinearEqs(A,b)
%LINEAREQS   線性方程式群組的求解
% X=LINEAREQS(A,B)  利用MATLAB附帶函數求線性方程式群組AX=B的解X
% [X,E]=LINEAREQS(A,B)  求線性方程式群組的解X並傳回其誤差
%
% 輸導入參數數：
%     ---A：方程式群組的系數矩陣
%     ---B：方程式群組的右端向量
% 輸出參數：
%     ---X：方程式群組的解
%     ---E：解的誤差
%
% See also null, inv(\), pinv

[m,n]=size(A);b=b(:);
if m~=length(b);
    error('系數矩陣A和右端向量b維數不符合.')
end
r1=rank(A);r2=rank([A b]);
if ~all(b)  % 齊次線性方程式群組
    if r1==n
        x=zeros(size(b));
    else
        z=null(sym(A));   %解出規範化的化零空間
        k=sym('k%d',[n-r1,1]);   %定義各基礎解系對應的系數
        x=z*k;   %原方程式的通解
    end
else  % 非齊次線性方程式群組
    if r1==r2&&r1==n
        disp('方程式群組是恰定的，有唯一解！')
        x=A\b;
    elseif r1==r2&&r1~=n
        disp('方程式群組是欠定的，有無窮解！')
        warning off all
        z=null(sym(A));   %解出規範化的化零空間
        x0=sym(A)\b;  %求出一個特解
        k=sym('k%d',[n-r1,1]);   %定義各基礎解系對應的系數
        x=x0+z*k;   %原方程式的通解
    else
        disp('方程式群組是超定的，只有最小二乘意義下的解！')
        x=pinv(A)*b;
    end
end
e=norm(double(A*x-b));