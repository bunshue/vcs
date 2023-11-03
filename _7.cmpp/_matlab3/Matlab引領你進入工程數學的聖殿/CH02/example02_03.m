x=input('x=');  y=input('y=');  % 提示輸入x、y
if x==0 | y==0  % 座標軸上的情形                
    f=0;                                 
elseif x<0 & y<0  % 第三象限                 
    f=x^2*y;                             
elseif x<0 & y>0  % 第二象限                 
    f=x*y^2;                             
elseif x>0 & y<0  % 第四象限                 
    f=x^2*y^2;                           
else             % 其他                    
    f=x^2*y^3;                           
end                                      
