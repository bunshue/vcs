function [x,y]=Explicit_Euler(odefun,xspan,y0,h,varargin)
%EXPLICIT_EULER   歐拉法求解初值問題的數值解
% [X,Y]=EXPLICIT_EULER(ODEFUN,XSPAN,Y0,H)  歐拉法求微分方程式ODEFUN的數值解
% [X,Y]=EXPLICIT_EULER(ODEFUN,XSPAN,Y0,H,P1,P2,...)  歐拉法求微分方程式ODEFUN
%                                      的數值解，ODEFUN含有附加參數P1,P2,...
%
% 輸導入參數數：
%     ---ODEFUN：微分方程式的函數描述
%     ---XSPAN：求解區間[x0,xn]
%     ---Y0：起始條件
%     ---H：迭代步長
%     ---P1,P2,...：ODEFUN函數的附加參數
% 輸出參數：
%     ---X：傳回的節點，即X=XSPAN(1):H:XSPAN(2)
%     ---Y：微分方程式的數值解
%
% See also ode*

x=xspan(1):h:xspan(2);
N=length(x);
y=zeros(1,N);
y(1)=y0;
for k=1:N-1
    y(k+1)=y(k)+h*feval(odefun,x(k),y(k),varargin{:});
end
x=x';y=y';