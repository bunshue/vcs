function S=SpecialMatrix(c,varargin)                                                  
%SPECIALMATRIX   產生Vandermonde矩陣、伴隨矩陣、Hankel矩陣以及托普利茨矩陣                                
% S=SPECIALMATRIX(C,TYPE)  利用向量C產生由TYPE特殊的特殊矩陣，可以產生數值矩陣或符號矩陣，                         
%                               TYPE有以下取值：                                            
%                               1.'compan'或1：伴隨矩陣                                     
%                               2.'vander'或2：Vandermonde矩陣                            
%                               3.'hankel'或3：Hankel矩陣                                 
%                               4.'toeplitz'或4：托普利茨矩陣                                 
% S=SPECIALMATRIX(C,R,TYPE)  利用向量C和R產生由TYPE特殊的特殊矩陣，                                   
%                                  TYPE此時只有'hankel'（3）和'toeplitz'（4）兩種取值              
%                                                                                     
% 輸導入參數數：                                                                               
%     ---C、R：產生特殊矩陣的控制向量                                                              
%     ---TYPE：特殊的特殊矩陣的型態字串或數字                                                        
% 輸出參數：                                                                               
%     ---S：傳回的特殊矩陣                                                                    
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
