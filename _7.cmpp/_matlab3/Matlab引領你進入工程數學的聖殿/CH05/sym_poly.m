function c=sym_poly(s,v,flag)                                
%SYM_POLY   符號多項式與多項式系數之間的相互轉換                               
% C=SYM_POLY(S,V,1)或C=SYM_POLY(S,V,'sym2poly')  分析符號多項式S的系數向量
% S=SYM_POLY(C,V,2)或S=SYM_POLY(C,V,'poly2sym')  由系數向量C建立符號多項式
%                                                            
% 輸導入參數數：                                                      
%     ---S：輸入的符號多項式                                          
%     ---V：符號多項式的符號自變數                                       
%     ---C：輸入的系數向量                                           
%     ---FLAG：指定轉化方向，當FLAG=1或'sym2poly'表示由多項式向系數向量轉化；        
%                當FLAG=2或'poly2sym'表示由系數向量向多項式轉化             
% 輸出參數：                                                      
%     ---C：傳回的符號多項式的系數向量                                     
%     ---S：由系數向量建立得到的符號多項式                                   
%                                                            
% See also poly2sym, sym2poly                                
                                                             
k=1;                                                         
switch flag                                                  
    case {1,'sym2poly'}                                      
        c=subs(s,v,0);                                       
        while 1                                              
            ds=diff(s,v);                                    
            c=[subs(ds,v,0)/prod(1:k),c];                    
            s=ds;                                            
            if ~ismember(sym(v),symvar(ds))                  
                break                                        
            end                                              
            k=k+1;                                           
        end                                                  
    case {2,'poly2sym'}                                      
        n=length(s);                                         
        c=s*(sym(v)).^(n-1:-1:0).';                          
    otherwise                                                
        error('Error flag.')                                 
end                                                          
