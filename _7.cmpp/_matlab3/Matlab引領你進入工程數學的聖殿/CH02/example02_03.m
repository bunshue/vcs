x=input('x=');  y=input('y=');  % ���ܿ�Jx�By
if x==0 | y==0  % �y�жb�W������                
    f=0;                                 
elseif x<0 & y<0  % �ĤT�H��                 
    f=x^2*y;                             
elseif x<0 & y>0  % �ĤG�H��                 
    f=x*y^2;                             
elseif x>0 & y<0  % �ĥ|�H��                 
    f=x^2*y^2;                           
else             % ��L                    
    f=x^2*y^3;                           
end                                      
