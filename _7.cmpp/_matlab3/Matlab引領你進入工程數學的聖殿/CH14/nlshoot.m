function [t,y] = nlshoot(f1,fv,tspan,x0f,tol,varargin)
%NLSHOOT   非線性邊值問題的打靶法求解
% [T,Y] = NLSHOOT(F1,FV,TSPAN,X0F,TOL)  打靶法求非線性邊值問題F1的解
% [T,Y] = NLSHOOT(F1,FV,TSPAN,X0F,TOL,P1,P2,...)  打靶法求非線性邊值問題F1的解，
%                                              其中F1，FV包括附加參數P1,P2,...
%
% 輸導入參數數：
%     ---F1,FV：微分方程式與前面介紹的關於變數v1,v2,v3,v4的微分方程式的函數描述
%     ---TSPAN：求解區間
%     ---X0F：指定的邊值條件
%     ---TOL：精度要求，用於控制參數m的誤差
%     ---P1,P2,...：函數F1和FV的附加參數
% 輸出參數：
%     ---T：傳回的節點
%     ---Y：邊值問題的解
%
% See also ode45, lineshoot

m0=1;  % m的初值
err=1;
while abs(err)>tol;
    [~,v] = ode45(fv,tspan,[x0f(1);m0;0;1],varargin);  % 計算迭代式
    m=m0-(v(end,1)-x0f(2))/v(end,3);  % 更新m的數值
    err=m-m0;
    m0=m;
end
[t,y] = ode45(f1,tspan,[x0f(1);m],varargin);  % 利用得到的初值求解方程式