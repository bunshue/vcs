function [dy,dx]=diff_ctr(y,dt,n)
%DIFF_CTR   數值微分求解
% [DY,DX]=DIFF_CTR(Y,DT,N)  利用中心差分算法求解離散資料Y的N解數值導數
%
% 輸導入參數數：
%     ---Y：指定的等間距的實驗資料
%     ---DT：自變數的間距
%     ---N：數值求導階次
% 輸出參數：
%     ---DY,DX：求得的導數向量與對應的自變數向量
%
% See also diff

yx1=[y 0 0 0 0 0];yx2=[0 y 0 0 0 0];yx3=[0 0 y 0 0 0];
yx4=[0 0 0 y 0 0];yx5=[0 0 0 0 y 0];yx6=[0 0 0 0 0 y];
switch n
    case 1
        dy=(-diff(yx1)+7*diff(yx2)+7*diff(yx3)-diff(yx4))/(12*dt);
        L0=3;
    case 2
        dy=(-diff(yx1)+15*diff(yx2)-15*diff(yx3)+diff(yx4))/(12*dt^2);
        L0=3;
    case 3
        dy=(-diff(yx1)+7*diff(yx2)-6*diff(yx3)-6*diff(yx4)+...
            7*diff(yx5)-diff(yx6))/(8*dt^3);L0=5;
    case 4
        dy=(-diff(yx1)+11*diff(yx2)-28*diff(yx3)+28*diff(yx4)-...
            11*diff(yx5)+diff(yx6))/(6*dt^4);L0=5;
end
dy=dy(L0+1:end-L0);
dx=((1:length(dy))+L0-2-(n>2))*dt;