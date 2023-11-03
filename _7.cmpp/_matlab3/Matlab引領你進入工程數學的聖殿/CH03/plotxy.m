function [AX,H1,H2]=plotxy(varargin)                                   
%PLOTXY   繪制雙座標系                                                       
% PLOTXY(X1,Y1,X2,Y2)  在雙座標系中使用plot函數分別繪制資料對X1-Y1和X2-Y2的圖形             
% PLOTXY(X1,Y1,X2,Y2,FUN)  在雙座標系中使用繪圖函數FUN分別繪制資料對X1-Y1和X2-Y2的          
%                               圖形，FUN可以是MATLAB附帶繪圖函數，例如plot、semilogx、 
%                               loglog、stem等，也可以是使用者自編繪圖函數，但該自編函數必須     
%                               具有形如h=function(x,y)的呼叫格式               
% PLOTXY(X1,Y1,X2,Y2,FUN1,FUN2)  在雙座標系中使用繪圖函數FUN1和FUN2分別繪制資料對X1-Y1     
%                                      和X2-Y2的圖形，其中FUN1和FUN2的格式與FUN完全一樣
% AX=PLOTXY(...)  繪制雙座標系圖形並傳回雙座標系的座標軸控制碼向量                              
% [AX,H1,H2]=PLOTXY(...)  繪制雙座標系圖形並傳回座標軸控制碼向量、座標軸中的圖形物件控制碼               
%                                                                      
% 輸導入參數數：                                                                
%     ---X1,Y1,X2,Y2：繪圖資料                                              
%     ---FUN,FUN1,FUN2：特殊的繪圖函數                                         
% 輸出參數：                                                                
%     ---AX：座標軸控制碼向量                                                    
%     ---H1,H2：兩座標系中的圖形物件控制碼                                            
%                                                                      
% See also PLOTYY                                                      
%                                                                      
args=varargin;                                                         
[x1,y1,x2,y2]=deal(args{1:4});                                         
if nargin<5, fun1 = @plot; else fun1 = args{5}; end                    
if nargin<6, fun2 = fun1;  else fun2 = args{6}; end                    
set(gcf,'NextPlot','add')                                              
hAxes1=axes;                                                           
h1=feval(fun1,hAxes1,x1,y1,'Color','b');                               
set(hAxes1,'XColor','b','YColor','b','Box','off')                      
hAxes2=axes('Position',get(hAxes1,'Position'));                        
h2=feval(fun2,hAxes2,x2,y2,'Color','r');                               
set(hAxes2,'Color','none','XColor','r','YColor','r','Box','off',...    
    'XAxisLocation','top','YAxisLocation','right')                     
if nargout==1                                                          
    AX=[hAxes1,hAxes2];                                                
elseif nargout==3                                                      
    AX=[hAxes1,hAxes2]; H1=h1; H2=h2;                                  
end                                                                    
