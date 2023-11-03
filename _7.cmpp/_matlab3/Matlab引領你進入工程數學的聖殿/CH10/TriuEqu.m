function x=TriuEqu(U,b)
%TRIUEQU   消去法求上三角方程式群組的解
% X=TRIUEQU(U,B)  消去法求方程式群組UX=B的解，其中U是上三角陣
%
% 輸導入參數數：
%     ---U：線性方程式群組的系數矩陣，是一個上三角矩陣
%     ---B：線性方程式群組的右端向量
% 輸出參數：
%     ---X：線性方程式群組的解
%
% See also Cramer

[m,n]=size(U);
if m~=n || length(b)~=m
    error('線性方程式群組的系數矩陣和常量項維數不符合.')
end
if isa([U,b(:)],'sym')
    x=sym(zeros(n,1));
else
    x=zeros(n,1);
end
x(n)=b(n)/U(n,n);  % 求x_n
for k=n-1:-1:1
    x(k)=(b(k)-U(k,k+1:n)*x(k+1:n))/U(k,k);  % 求x_k，k=n-1,n-2,…,1
end