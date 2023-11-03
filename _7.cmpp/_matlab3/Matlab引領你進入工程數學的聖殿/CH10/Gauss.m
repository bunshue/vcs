function [x,U]=Gauss(A,b)
%GAUSS   高斯消去法求線性方程式群組的解
% X=GAUSS(A,B)  高斯消去法求線性方程式群組AX=B的解X
% [X,U]=GAUSS(A,B)  高斯消去法求線性方程式群組AX=B的解X並傳回消去後的上三角方程式群組的增廣矩陣
%
% 輸導入參數數：
%     ---A：線性方程式群組的系數矩陣
%     ---B：線性方程式群組的右端項
% 輸出參數：
%     ---X：線性方程式群組的解
%     ---U：消去後的上三角方程式群組的增廣矩陣
%
% See also TriuEqu

[m,n]=size(A);
if m~=n || length(b)~=m
    error('線性方程式群組的系數矩陣和常量項維數不符合.')
end
% 消去過程
for k=1:n-1
    m=A(k+1:n,k)/A(k,k);
    A(k+1:n,k+1:n)=A(k+1:n,k+1:n)-m*A(k,k+1:n);
    b(k+1:n)=b(k+1:n)-m*b(k);
    if isa([A,b(:)],'sym')
        A(k+1:n,k)=sym(zeros(n-k,1));
    else
        A(k+1:n,k)=zeros(n-k,1);
    end
end
U=[A,b];
x=TriuEqu(A,b);