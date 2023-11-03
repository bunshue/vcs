function xi=Cauchy(fx,Fx,range)                                 
%CAUCHY   驗證函數在某個區間上是否滿足柯西中值定理                                  
% CAUCHY(F,G,RANGE)  以圖形的模式示範函數在某個區間上的柯西中值定理                    
% XI=CAUCHY(F,G,RANGE)  傳回函數在指定區間上的一個柯西中值點                      
%                                                               
% 輸導入參數數：                                                         
%     ---F,G：函數的MATLAB描述，可以是匿名函數、內聯函數和M檔案                       
%     ---RANGE：特殊的區間                                            
% 輸出參數：                                                         
%     ---XI：柯西中值點                                               
%                                                               
% Sea also Rolle, Lagange                                       
                                                                
fab=subs(fx,range);                                             
Fab=subs(Fx,range);                                             
df=diff(fx);                                                    
dF=diff(Fx);                                                    
while 1                                                         
    x=fzero(inline(df/dF-diff(fab)/diff(Fab)),rand);            
    if prod(subs(Fx,x)-range)<=0                                
        break                                                   
    end                                                         
end                                                             
if nargout==1                                                   
    xi=x;                                                       
else                                                            
    ezplot(Fx,fx,range)                                         
    hold on                                                     
    x_range=[subs(Fx,x)-diff(Fab)/10,subs(Fx,x)+diff(Fab)/10];  
    y_range=diff(fab)/diff(Fab)*(x_range-subs(Fx,x))+subs(fx,x);
    plot(x_range,y_range,'k--')                                 
    title(['\xi=',num2str(x)])                                  
end                                                             
