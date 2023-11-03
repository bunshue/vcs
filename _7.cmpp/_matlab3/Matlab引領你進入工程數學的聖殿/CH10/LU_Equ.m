function [x,L,U]=LU_Equ(A,b)
%LU_EQU   LU分解法求線性方程式群組的解
% X=LU_EQU(A,B)  LU分解法求線性方程式群組AX=B的解X
% [X,L,U]=LU_EQU(A,B)  LU分解法求線性方程式群組AX=B的解X，並傳回分解後的上(下)三角矩陣
%
% 輸導入參數數：
%     ---A：線性方程式群組的系數矩陣
%     ---B：線性方程式群組的右端項
% 輸出參數：
%     ---X：線性方程式群組的解
%     ---L：分解後的下三角矩陣
%     ---U：分解後的上三角矩陣
%
% See also TriuEqu

[m,n]=size(A);
if m~=n || length(b)~=m
    error('線性方程式群組的系數矩陣和常量項維數不符合.')
end
if isa([A,b(:)],'sym')
    U=sym(zeros(n));
    L=sym(eye(n));
else
    U=zeros(n);
    L=eye(n);
end
U(1,:)=A(1,:);
L(2:n,1)=A(2:n,1)/U(1,1);
for k=2:n
    U(k,k:n)=A(k,k:n)-L(k,1:k-1)*U(1:k-1,k:n);
    L(k+1:n,k)=A(k+1:n,k)-L(k+1:n,1:k-1)*U(1:k-1,k);
    L(k+1:n,k)=L(k+1:n,k)/U(k,k);
end
y=flipud(TriuEqu(rot90(L,2),flipud(b(:))));
x=TriuEqu(U,y);