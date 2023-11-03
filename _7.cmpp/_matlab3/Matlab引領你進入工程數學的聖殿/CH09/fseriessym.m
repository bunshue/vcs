function [A,B,F]=fseriessym(f,x,n,a,b)
%FSERIESSYM   傅裡葉級數的符號求解
% [A,B,F]=FSERIESSYM(FUN,X,N)  將函數FUN在區間[-pi,pi]上展成N階傅裡葉級數
% [A,B,F]=FSERIESSYM(FUN,X,N,ALPHA,BETA)  將函數FUN在指定區間上展成N階傅裡葉級數
%
% 輸導入參數數：
%     ---FUN：指定的待展開函數
%     ---X：自變數
%     ---N：展開項數
%     ---ALPHA,BETA：級數展開區間，預設值為[-pi,pi]
% 輸出參數：
%     ---A,B：傅裡葉系數向量
%     ---F：函數的傅裡葉展開式
%
% See also int

if nargin==3
    a=-pi;b=pi; 
end
L=(b-a)/2; 
A=int(f,x,-L,L)/L;
B=[];F=A/2;
for k=1:n
   ak=int(f*cos(k*pi*x/L),x,-L,L)/L;
   bk=int(f*sin(k*pi*x/L),x,-L,L)/L;
   A=[A,ak];
   B=[B,bk];
   F=F+ak*cos(k*pi*x/L)+bk*sin(k*pi*x/L);
end