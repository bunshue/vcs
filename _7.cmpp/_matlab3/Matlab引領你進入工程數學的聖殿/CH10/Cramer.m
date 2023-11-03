function x=Cramer(A,b)
%CRAMER   克萊姆法則求恰定線性方程式群組的解
% X=CRAMER(A,B)  克萊姆法則求線性方程式群組AX=B的解X
%
% 輸導入參數數：
%     ---A：線性方程式群組的系數矩陣
%     ---B：線性方程式群組的右端向量
% 輸出參數：
%     ---X：線性方程式群組的解
%
% See also det

[m,n]=size(A);
if m~=n || length(b)~=m
    error('線性方程式群組的系數矩陣和常量項維數不符合.')
end
if isa([A,b(:)],'sym')
    x=sym(zeros(n,1));
else
    x=zeros(n,1);
end
D=det(A);
for k=1:n
    Dk=A;
    Dk(:,k)=b(:);
    Dk=det(Dk);
    x(k)=Dk/D;
end