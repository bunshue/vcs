function [t,y] = lineshoot(f1,f2,tspan,x0f,varargin)
%LINESHOOT   線性邊值問題的打靶法求解
% [T,Y] = LINESHOOT(F1,F2,TSPAN,X0F)  打靶法求線性邊值問題F1的解
% [T,Y] = LINESHOOT(F1,F2,TSPAN,X0F,P1,P2,...)  打靶法求線性邊值問題F1的解，其中
%                                               F1和F2包括附加參數P1,P2,...
%
% 輸導入參數數：
%     ---F1,F2：微分方程式及其對應齊次方程式的函數描述
%     ---TSPAN：求解區間
%     ---X0F：邊值條件
%     ---P1,P2,...：函數F1和F2的附加參數
% 輸出參數：
%     ---T：傳回的節點
%     ---Y：邊值問題的解
%
% See also ode45

[~,y1] = ode45(f2,tspan,[1;0],varargin);  % 計算函數y_1(t)
[~,y2] = ode45(f2,tspan,[0;1],varargin);  % 計算函數y_2(t)
[~,yp] = ode45(f1,tspan,[0;0],varargin);  % 計算函數y_p(t)
m = (x0f(2)-x0f(1)*y1(end,1)-yp(end,1))/y2(end,1);  % 求參數m
[t,y] = ode45(f1,tspan,[x0f(1);m],varargin);  % 求出原微分方程式的解