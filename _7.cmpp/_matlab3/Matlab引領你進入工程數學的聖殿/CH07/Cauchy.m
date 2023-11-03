function xi=Cauchy(fx,Fx,range)                                 
%CAUCHY   ���Ҩ�Ʀb�Y�Ӱ϶��W�O�_�����_�褤�ȩw�z                                  
% CAUCHY(F,G,RANGE)  �H�ϧΪ��Ҧ��ܽd��Ʀb�Y�Ӱ϶��W���_�褤�ȩw�z                    
% XI=CAUCHY(F,G,RANGE)  �Ǧ^��Ʀb���w�϶��W���@�Ӭ_�褤���I                      
%                                                               
% ��ɤJ�ѼƼơG                                                         
%     ---F,G�G��ƪ�MATLAB�y�z�A�i�H�O�ΦW��ơB���p��ƩMM�ɮ�                       
%     ---RANGE�G�S���϶�                                            
% ��X�ѼơG                                                         
%     ---XI�G�_�褤���I                                               
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
