disp([repmat('=',1,34),'九九乘法表',repmat('=',1,34)])
for r=1:9                                        
    for c=1:r                                    
        p=r*c;                                   
        fprintf('%d×%d=%2d  ',c,r,p)             
    end                                          
    fprintf('\n')                                
end                                              
