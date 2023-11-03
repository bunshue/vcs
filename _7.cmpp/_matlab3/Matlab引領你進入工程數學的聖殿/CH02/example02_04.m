month=input('請輸入月份month=');  % 提示輸入月份            
if month>12 || month<1 || mod(month,1)~=0  % 判斷條件
    error('輸入的月份必須是1~12的整數！')  % 不符合條件則舉出錯誤提示    
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
