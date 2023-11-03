function C=mat_add(varargin)                    
%MAT_ADD   ―ヴ種蝴计痻皚㎝                         
% C=MAT_ADD(A,B,...)  璸衡痻皚㎝                  
%                                               
% 块旧把计计                                         
%     ---A,B,...蝴计痻皚                        
% 块把计                                         
%     ---C肚㎝痻皚                               
                                                
error(nargchk(2,inf,nargin))                    
C=varargin{1};                                  
s=size(C);                                      
for k=2:numel(varargin)                         
    B=varargin{k};                              
    s1=size(B);                                 
    if isequal(s,s1)                            
        C=C+B;                                  
    else                                        
        error('Martix dimension does''t match.')
    end                                         
end                                             
