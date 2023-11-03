function C=mat_add(varargin)                    
%MAT_ADD   �D���N�ӬۦP���Ưx�}���M                         
% C=MAT_ADD(A,B,...)  �p��h�ӯx�}���M                  
%                                               
% ��ɤJ�ѼƼơG                                         
%     ---A,B,...�G���ƬۦP���x�}                        
% ��X�ѼơG                                         
%     ---C�G�Ǧ^���M�x�}                               
                                                
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
