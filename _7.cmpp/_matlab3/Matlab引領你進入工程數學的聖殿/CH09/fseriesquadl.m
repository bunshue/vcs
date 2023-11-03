function [A,B,F] = fseriesquadl(fun,x,n,a,b)
%FSERIESQUADL   傅裡葉級數的數值求解
% [A,B,F]=FSERIESQUADL(FUN,X,N)  求函數FUN在區間[-pi,pi]上的N階數值傅裡葉展式
% [A,B,F]=FSERIESQUADL(FUN,X,N,ALPHA,BETA)  求函數FUN在指定區間上的數值傅裡葉展式
%
% 輸導入參數數：
%     ---FUN：指定的待展開函數
%     ---X：自變數資料
%     ---N：展開項數
%     ---ALPHA,BETA：級數展開區間，預設值為[-pi,pi]
% 輸出參數：
%     ---A,B：傅裡葉系數向量
%     ---F：函數的傅裡葉展開式在X上的值
%
% See also quadl, fseriessym

if nargin==3
    a=-pi;b=pi; 
end
L=(b-a)/2;
f=inline(fun);
var=char(argnames(f));
A=zeros(1,n+1);B=zeros(1,n);
A(1) = quadl(f,-L,L)/L; % 計算A_0
F=A(1)/2;
for k=1:n;
    fcos=inline(['(',fun,')','.*cos(',num2str(k*pi/L),'*',var,')']); 
    fsin=inline(['(',fun,')','.*sin(',num2str(k*pi/L),'*',var,')']); 
    A(k+1) =quadl(fcos,-L,L)/L;  % 計算系數A(2:n+1)
    B(k)=quadl(fsin,-L,L)/L;  % 計算系數B(1:n)
    F=F+A(k+1)*cos(k*pi*x/L)+B(k)*sin(k*pi*x/L);
end