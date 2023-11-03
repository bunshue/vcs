function S=SpecialMatrix(c,varargin)                                                  
%SPECIALMATRIX   ����Vandermonde�x�}�B���H�x�}�BHankel�x�}�H�Φ����Q���x�}                                
% S=SPECIALMATRIX(C,TYPE)  �Q�ΦV�qC���ͥ�TYPE�S���S��x�}�A�i�H���ͼƭȯx�}�βŸ��x�}�A                         
%                               TYPE���H�U���ȡG                                            
%                               1.'compan'��1�G���H�x�}                                     
%                               2.'vander'��2�GVandermonde�x�}                            
%                               3.'hankel'��3�GHankel�x�}                                 
%                               4.'toeplitz'��4�G�����Q���x�}                                 
% S=SPECIALMATRIX(C,R,TYPE)  �Q�ΦV�qC�MR���ͥ�TYPE�S���S��x�}�A                                   
%                                  TYPE���ɥu��'hankel'�]3�^�M'toeplitz'�]4�^��ب���              
%                                                                                     
% ��ɤJ�ѼƼơG                                                                               
%     ---C�BR�G���ͯS��x�}������V�q                                                              
%     ---TYPE�G�S���S��x�}�����A�r��μƦr                                                        
% ��X�ѼơG                                                                               
%     ---S�G�Ǧ^���S��x�}                                                                    
%                                                                                     
% See also compan, vander, hankel, toeplitz                                           
                                                                                      
str={'compan','vander','hankel','toeplitz'};                                          
type=varargin{end};                                                                   
if isnumeric(type)                                                                    
    type=str{type};                                                                   
end                                                                                   
if isnumeric(c)                                                                       
    S=feval(type,c,varargin{1:end-1});                                                
else                                                                                  
    c=c(:);                                                                           
    nc=length(c);                                                                     
    switch lower(type)                                                                
        case 'compan'                                                                 
            c=c.';                                                                    
            S=sym(diag(ones(1,nc-2),-1));                                             
            S(1,:)=-c(2:end)/c(1);                                                    
        case 'vander'                                                                 
            S=sym(ones(nc));                                                          
            for j=nc-1:-1:1                                                           
                S(:,j)=c.*S(:,j+1);                                                   
            end                                                                       
        case 'hankel'                                                                 
            if numel(varargin)<2                                                      
                r = zeros(size(c));                                                   
            else                                                                      
                r=varargin{1};                                                        
            end                                                                       
            if c(nc)~=r(1)                                                            
                warning(['MATLAB:',upper(type),':AntiDiagonalConflict'],...           
                    ['Last element of input column does not match first element ' ... 
                    'of input row. \nColumn wins anti-diagonal conflict.'])           
            end                                                                       
            r=r(:);                                                                   
            nr=length(r);                                                             
            x=[c; r((2:nr)')];                                                        
            cidx=(1:nc)';                                                             
            ridx=0:(nr-1);                                                            
            H=cidx(:,ones(nr,1))+ridx(ones(nc,1),:);                                  
            S=x(H);                                                                   
        case 'toeplitz'                                                               
            if numel(varargin)<2                                                      
                c(1)=conj(c(1)); r=c; c=conj(c);                                      
            else                                                                      
                r=varargin{1};                                                        
            end                                                                       
            if r(1)~=c(1)                                                             
                warning(['MATLAB:',upper(type),':DiagonalConflict'],...               
                    ['First element of input column does not match first element ' ...
                    ' of input row. \nColumn wins diagonal conflict.'])               
            end                                                                       
            r=r(:);                                                                   
            nr=length(r);                                                             
            x = [r(nr:-1:2) ; c];                                                     
            cidx = (0:nc-1)';                                                         
            ridx = nr:-1:1;                                                           
            t = cidx(:,ones(nr,1)) + ridx(ones(nc,1),:);                              
            S = x(t);                                                                 
        otherwise                                                                     
            error('Illegal options.')                                                 
    end                                                                               
end                                                                                   
