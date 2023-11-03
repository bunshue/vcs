function print_matrix(c)                                                             
%PRINT_MATRIX   �C�L�p�k�Φ����x�}                                            A               
% PRINT_MATRIX(C)  �ھڿ�J����ƩΦr�����ͥk��Φ����r���x�}              B B B                          
%                                                                           C C C C C
% ��ɤJ�ѼƼơG                                                                  B B B       
%     ---C�G���N��ƩΤj�p�g�r��                                                A               
%                                                                                    
% See also fprintf                                                                   
                                                                                     
if isnumeric(c)                                                                      
    c=char(mod(fix(c)-1,26)+'A');                                                    
elseif ischar(c)                                                                     
    if length(c)>1 || ~((c>'a' && c<'z') || (c>'A' && c<'Z'))                        
        error('Input argument must be a letter.')                                    
    else                                                                             
        c=upper(c);                                                                  
    end                                                                              
end                                                                                  
N=c-'A'+1;                                                                           
str=blanks(4*N-3);                                                                   
S=[];                                                                                
for k=1:N                                                                            
    str(2*N-1-2*(k-1):2:2*N-1+2*(k-1))=repmat(char('A'+k-1),1,2*k-1);                
    S=[S;str];                                                                       
end                                                                                  
for kk=1:2*N-1                                                                       
    if kk<=N                                                                         
        fprintf('%s\n',S(kk,:))                                                      
    else                                                                             
        fprintf('%s\n',S(2*N-kk,:))                                                  
    end                                                                              
end                                                                                  
