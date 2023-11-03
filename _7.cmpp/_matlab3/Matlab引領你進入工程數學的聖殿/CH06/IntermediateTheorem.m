function xi=IntermediateTheorem(fun,range,C)
%INTERMEDIATETHEOREM   驗證連續函數的介值定理
% IntermediateTheorem(FUN,RANGE,C)  以圖形的形式驗證連續函數在閉區間上的介值定理
% XI=IntermediateTheorem(FUN,RANGE,C)  傳回連續函數的一個介值點，但不繪制圖形
%
% 輸導入參數數：
%     ---FUN：連續函數的表達式
%     ---RANGE：特殊的區間[a,b]
%     ---C：介於FUN(a)與FUN(b)的任意實數
% 輸出參數：
%     ---XI：XI滿足FUN(XI)=C，若為指定輸出則以圖形模式驗證
%
% See also fzero

if nargin==2
    C=0;
end
fab=feval(fun,range);
if prod(fab-C)<=0  % 判斷C是否屬於f(a)和f(b)之間
    if fab(1)==0
        x0=range(1);
    elseif fab(2)==0
        x0=range(2);
    else
        x0=fzero(@(x)fun(x)-C,range);
    end
else
    return
end
if nargout==1  % 判斷輸出參數個數
    xi=x0;
else
    fplot(fun,range)
    hold on
    plot(xlim,[C,C],'k--')
    plot(x0,fun(x0),'k*')
    title(['\xi=',num2str(x0)])
end
