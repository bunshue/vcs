function [x,y]=Classical_RK4(odefun,xspan,y0,h,varargin)
%CLASSICAL_RK4   經典四階Runge-Kutta法求解初值問題的數值解
% [X,Y]=CLASSICAL_RK4(ODEFUN,XSPAN,Y0,H)  經典四階Runge-Kutta法求解微分方程式ODEFUN
% [X,Y]=CLASSICAL_RK4(ODEFUN,XSPAN,Y0,H,P1,P2,...)  經典四階Runge-Kutta法求解
%                                  微分方程式ODEFUN，ODEFUN包括附加參數P1,P2,...
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
% See also Explicit_Euler

x=xspan(1):h:xspan(2);
N=length(x);
y=zeros(1,N);
y(1)=y0;
for k=1:length(x)-1
    K1=feval(odefun,x(k),y(k),varargin{:});
    K2=feval(odefun,x(k)+h/2,y(k)+h/2*K1,varargin{:});
    K3=feval(odefun,x(k)+h/2,y(k)+h/2*K2,varargin{:});
    K4=feval(odefun,x(k)+h,y(k)+h*K3,varargin{:});
    y(k+1)=y(k)+h/6*(K1+2*K2+2*K3+K4);
end
x=x';y=y';