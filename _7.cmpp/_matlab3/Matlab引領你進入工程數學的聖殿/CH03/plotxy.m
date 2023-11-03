function [AX,H1,H2]=plotxy(varargin)                                   
%PLOTXY   ø�����y�Шt                                                       
% PLOTXY(X1,Y1,X2,Y2)  �b���y�Шt���ϥ�plot��Ƥ��Oø���ƹ�X1-Y1�MX2-Y2���ϧ�             
% PLOTXY(X1,Y1,X2,Y2,FUN)  �b���y�Шt���ϥ�ø�Ϩ��FUN���Oø���ƹ�X1-Y1�MX2-Y2��          
%                               �ϧΡAFUN�i�H�OMATLAB���aø�Ϩ�ơA�Ҧpplot�Bsemilogx�B 
%                               loglog�Bstem���A�]�i�H�O�ϥΪ̦۽sø�Ϩ�ơA���Ӧ۽s��ƥ���     
%                               �㦳�Φph=function(x,y)���I�s�榡               
% PLOTXY(X1,Y1,X2,Y2,FUN1,FUN2)  �b���y�Шt���ϥ�ø�Ϩ��FUN1�MFUN2���Oø���ƹ�X1-Y1     
%                                      �MX2-Y2���ϧΡA�䤤FUN1�MFUN2���榡�PFUN�����@��
% AX=PLOTXY(...)  ø�����y�Шt�ϧΨöǦ^���y�Шt���y�жb����X�V�q                              
% [AX,H1,H2]=PLOTXY(...)  ø�����y�Шt�ϧΨöǦ^�y�жb����X�V�q�B�y�жb�����ϧΪ��󱱨�X               
%                                                                      
% ��ɤJ�ѼƼơG                                                                
%     ---X1,Y1,X2,Y2�Gø�ϸ��                                              
%     ---FUN,FUN1,FUN2�G�S��ø�Ϩ��                                         
% ��X�ѼơG                                                                
%     ---AX�G�y�жb����X�V�q                                                    
%     ---H1,H2�G��y�Шt�����ϧΪ��󱱨�X                                            
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
