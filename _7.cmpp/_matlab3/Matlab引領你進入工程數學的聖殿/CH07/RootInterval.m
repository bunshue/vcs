function r=RootInterval(fun,a,b,h)
%ROOTINTERVAL   逐步掃描法求方程式的隔根區間
% R=ROOTINTERVAL(FUN,A,B)
% R=ROOTINTERVAL(FUN,A,B,H)
%
% 輸導入參數數：
%     ---FUN：方程式的MATLAB描述，可以為匿名函數或內聯函數
%     ---A,B：區間端點
%     ---H：步長
% 輸出參數：
%     ---R：傳回的隔根區間，是一個列數為2的矩陣

if nargin==3
    h=(b-a)/100;
end
a1=a;b1=a1+h;
r=[];
while b1<b
    if fun(a1)*fun(b1)<0
        r=[r;[a1,b1]];
        a1=b1;b1=a1+h;
    else
        a1=b1;b1=a1+h;
        continue
    end
end