function S = summation(n)                          
%SUMMATION   �D�M��1+2*3+3*4+4*5+...                  
% S=SUMMATION(N)  �Q�λ��k��k�D�M1+2*3+3*4+4*5+...+N*(N+1)
%                                                  
% ��ɤJ�ѼƼơG                                            
%     ---N�G����                                      
% ��X�ѼơG                                            
%     ---S�G�M�����M                                    
%                                                  
% See also sum, prod                               
                                                   
if n==1                                            
    S=1;                                           
else                                               
    S=n*(n+1)+summation(n-1);                      
end                                                
