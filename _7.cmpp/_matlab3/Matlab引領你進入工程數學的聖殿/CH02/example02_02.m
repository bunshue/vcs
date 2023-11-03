c=input('請輸入一個字元:','s');  % 提示輸入字元           
if c>='A' && c<='Z'                          
   disp(char(c+'a'-'A'));        % 輸出c對應的小寫字元
elseif c>='a'&& c<='z'                       
    disp(char(c-'a'+'A'));   % 輸出c對應的大寫字元    
elseif c>='0'&& c<='9'                       
    disp(c-'0');           % 輸出c對應的數字        
else                                         
    disp(c);                 % 輸出c           
end                                          
