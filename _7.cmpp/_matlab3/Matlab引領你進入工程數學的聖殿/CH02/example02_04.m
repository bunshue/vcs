month=input('�п�J���month=');  % ���ܿ�J���            
if month>12 || month<1 || mod(month,1)~=0  % �P�_����
    error('��J����������O1~12����ơI')  % ���ŦX����h�|�X���~����    
end                                              
switch month                                     
    case {3 4 5}                                 
        season='spring';                         
    case {6 7 8}                                 
        season='summer';                         
    case {9 10 11}                               
        season='autumn';                         
    otherwise                                    
        season='winter';                         
end                                              
