function A=CircleArea(R,n)
%CIRCLEAREA   圓面積的無限逼近計算
% A=CIRCLEAREA(R,N)  利用多邊形面積無限逼近圓的面積
%
% 輸導入參數數：
%     ---R：圓的半徑
%     ---N：正多邊形邊數
% 輸出參數：
%     ---A：圓的近似面積
%
% See also symsum

M=R;
A=sqrt(3)/4*M^2*6;
for k=2:n
    G=sqrt(R^2-(M/2)^2);
    j=R-G;
    m=sqrt((M/2)^2+j^2);
    a=1/2*M*j*3*2^(k-1);
    M=m;
    A=A+a;
end
if isa(R,'sym')
    A=simple(A);
end