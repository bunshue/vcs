c=input('�п�J�@�Ӧr��:','s');  % ���ܿ�J�r��           
if c>='A' && c<='Z'                          
   disp(char(c+'a'-'A'));        % ��Xc�������p�g�r��
elseif c>='a'&& c<='z'                       
    disp(char(c-'a'+'A'));   % ��Xc�������j�g�r��    
elseif c>='0'&& c<='9'                       
    disp(c-'0');           % ��Xc�������Ʀr        
else                                         
    disp(c);                 % ��Xc           
end                                          
