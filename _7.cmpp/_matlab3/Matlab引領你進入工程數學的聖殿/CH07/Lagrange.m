function xi=Lagrange(fun,range)
%LAGRANGE   驗證函數在某個區間上是否滿足拉格朗日中值定理
% LAGRANGE(FUN,RANGE)  以圖形的模式示範函數在某個區間上的拉格朗日中值定理
% XI=LAGRANGE(FUN,RANGE)  傳回函數在指定區間上的一個拉格朗日中值點
%
% 輸導入參數數：
%     ---FUN：函數的MATLAB描述，可以是匿名函數、內聯函數和M檔案
%     ---RANGE：特殊的區間
% 輸出參數：
%     ---XI：拉格朗日中值點
%
% Sea also Rolle

fab=subs(fun,range);
df=diff(fun);
while 1
    x=fzero(inline(df-diff(fab)/diff(range)),rand);
    if prod(x-range)<=0
        break
    end
end
if nargout==1
    xi=x;
else
    ezplot(fun,range)
    hold on
    x_range=[x-diff(range)/10,x+diff(range)/10];
    y_range=diff(fab)/diff(range)*(x_range-x)+subs(fun,x);
    plot(x_range,y_range,'k--')
    title(['\xi=',num2str(x)])
end
