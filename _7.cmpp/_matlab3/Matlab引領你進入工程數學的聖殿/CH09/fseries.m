function [A,B,F,type]=fseries(f,x,n,a,b)
%FSERIES   傅裡葉級數求解，並傳回傅裡葉級數的型態
% [A,B,F]=FSERIES(FUN,X,N)  求奇(或偶)函數FUN在區間[-pi,pi]上的N階傅裡葉展式
% [A,B,F]=FSERIES(FUN,X,N,ALPHA,BETA)  求奇(或偶)函數FUN在指定區間上的N階傅裡葉展式
% [A,B,F,TYPE]=FSERIES(...)  求函數的傅裡葉展式並傳回傅裡葉級數型態
%
% 輸導入參數數：
%     ---FUN：指定的待展開函數
%     ---X：自變數
%     ---N：展開項數
%     ---ALPHA,BETA：級數展開區間，預設值為[-pi,pi]
% 輸出參數：
%     ---A,B：傅裡葉系數向量
%     ---F：函數的傅裡葉展開式
%     ---TYPE：傅裡葉級數型態字串
%
% See also int, fseriessym, fseriesquadl

if nargin==3
    a=-pi;b=pi;
end
L=(b-a)/2;
f1=subs(f,-x);
A=sym(zeros(1,n+1));
B=sym(zeros(1,n));
F=0;
if isequal(simple(f+f1),0)  % 奇函數
    for k=1:n
        B(k)=2*int(f*sin(k*pi*x/L),x,0,L)/L;
        F=F+B(k)*sin(k*pi*x/L);
    end
    type='正弦級數';
elseif isequal(f,f1)  % 偶函數
    for k=0:n
        A(k+1)=2*int(f*cos(k*pi*x/L),x,0,L)/L;
        F=F+A(k+1)*cos(k*pi*x/L);
    end
    type='余弦級數';
else  % 一般函數
    A(1)=int(f,x,-L,L)/L;
    F=A(1)/2;
    for k=1:n
        A(k+1)=int(f*cos(k*pi*x/L),x,-L,L)/L;
        B(k)=int(f*sin(k*pi*x/L),x,-L,L)/L;
        F=F+A(k+1)*cos(k*pi*x/L)+B(k)*sin(k*pi*x/L);
    end
    type='一般三角級數';
end