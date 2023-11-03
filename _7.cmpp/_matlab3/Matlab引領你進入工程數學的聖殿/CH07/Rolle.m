function varargout=Rolle(fun,range)
%ROLLE   驗證函數在某個區間上是否滿足羅爾定理
% ROLLE(FUN,RANGE)  以圖形的模式示範函數在某個區間上的羅爾定理
% TF=ROLLE(FUN,RANGE)  以圖形的模式示範函數在某個區間傷的羅爾定理，
%                          並傳回表征函數是否滿足羅爾定理的量，TF=1滿足；TF=0不滿足
% [TF,XI]=ROLLE(FUN,RANGE)  傳回表征函數在指定區間上是否滿足羅爾定理的量TF和一個羅爾點
%
% 輸導入參數數：
%     ---FUN：函數的MATLAB描述，可以是匿名函數、內聯函數和M檔案
%     ---RANGE：特殊的區間
% 輸出參數：
%     ---TF：表征是否滿足羅爾定理的量
%     ---XI：羅爾點
%
% See also fzero

fab=subs(fun,range);
tf=0;
if fab(1)~=fab(2)
    disp('函數fun在區間range上不滿足羅爾定理.')
    return
else
    tf=1;
end
df=diff(fun);
while 1
    xi=fzero(inline(df),rand);
    if prod(xi-range)<=0
        break
    end
end
if nargout==2 && tf==1
    varargout{1}=tf;
    varargout{2}=xi;
else
    varargout{1}=tf;
    ezplot(fun,range)
    hold on
    plot([xi-diff(range)/10,xi+diff(range)/10],[0,0],'k--')
    title(['\xi=',num2str(xi)])
end
