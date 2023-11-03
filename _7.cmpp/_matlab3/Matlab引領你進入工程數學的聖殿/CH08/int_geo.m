function [I,Interval,s]=int_geo(fun,a,b,N)
%INT_GEO  根據定積分的幾何意義求定積分
% I=INT_GEO(FUN,A,B)  利用定積分的幾何意義計算函數FUN的積分值，積分上下限分別為B和A
% I=INT_GEO(FUN,A,B,N)  利用定積分的幾何意義計算定積分，區間等分數為N
% [I,INTERVAL]=INT_GEO(...)  利用定積分的幾何意義計算定積分，並傳回恆正或恆負區間
% [I,INTERVAL,S]=INT_GEO(...)  利用定積分的幾何意義計算定積分，並傳回恆正或恆負區間
%                                    以及對應區間上的積分值
%
% 輸導入參數數：
%     ---FUN：函數的MATLAB描述，可以為匿名函數、內聯函數或M檔案
%     ---A,B：積分下限和上限
%     ---N：各恆正或恆負區間等分數
% 輸出參數：
%     ---I：積分值
%     ---INTERVAL：恆正或恆負區間
%     ---S：各區間上的積分值
%
% See also RootInterval, bisect, diff

if nargin<4
    N=1000;
end
r=RootInterval(fun,a,b);
if ~isempty(r)
    n=size(r,1);
    x=ones(1,n+2);
    x(1)=a; x(end)=b;
    for k=1:n
        x(k+1)=bisect(fun,r(k,1),r(k,2));
    end
    x=unique(x);
    L=length(x);
    Interval=zeros(2,L-1);
    for kk=1:L-1
        Interval(:,kk)=x(kk:kk+1);
    end
else
    Interval=[a;b];
end
h=diff(Interval)/N;
M=mean(Interval);
fM=feval(fun,M);
fM(fM>0)=1;
fM(fM<0)=-1;
s=zeros(1,size(Interval,2));
for k=1:size(Interval,2)
    xx=Interval(1,k)+h(k)*(0:N);
    fx=abs(feval(fun,xx));
    s(k)=sum(fx)*h(k);
end
I=sum(s.*fM);