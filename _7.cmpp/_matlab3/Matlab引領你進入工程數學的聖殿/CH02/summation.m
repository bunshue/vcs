function S = summation(n)                          
%SUMMATION   ―㎝Α1+2*3+3*4+4*5+...                  
% S=SUMMATION(N)  ノ患耴衡猭―㎝1+2*3+3*4+4*5+...+N*(N+1)
%                                                  
% 块旧把计计                                            
%     ---N兜计                                      
% 块把计                                            
%     ---S㎝Α㎝                                    
%                                                  
% See also sum, prod                               
                                                   
if n==1                                            
    S=1;                                           
else                                               
    S=n*(n+1)+summation(n-1);                      
end                                                
