function c=sym_poly(s,v,flag)                                
%SYM_POLY   �Ÿ��h�����P�h�����t�Ƥ������ۤ��ഫ                               
% C=SYM_POLY(S,V,1)��C=SYM_POLY(S,V,'sym2poly')  ���R�Ÿ��h����S���t�ƦV�q
% S=SYM_POLY(C,V,2)��S=SYM_POLY(C,V,'poly2sym')  �Ѩt�ƦV�qC�إ߲Ÿ��h����
%                                                            
% ��ɤJ�ѼƼơG                                                      
%     ---S�G��J���Ÿ��h����                                          
%     ---V�G�Ÿ��h�������Ÿ����ܼ�                                       
%     ---C�G��J���t�ƦV�q                                           
%     ---FLAG�G���w��Ƥ�V�A��FLAG=1��'sym2poly'��ܥѦh�����V�t�ƦV�q��ơF        
%                ��FLAG=2��'poly2sym'��ܥѨt�ƦV�q�V�h�������             
% ��X�ѼơG                                                      
%     ---C�G�Ǧ^���Ÿ��h�������t�ƦV�q                                     
%     ---S�G�Ѩt�ƦV�q�إ߱o�쪺�Ÿ��h����                                   
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
