s=input('�п�J����G','s');                                 
for k=1:length(s)                                      
    if s(k)>='a' && s(k)<='z' || s(k)>='A' && s(k)<='Z'
        s(k)=s(k)+4;                                   
        if s(k)>'Z' && s(k)<='Z'+4 || s(k)>'z'         
            s(k)=s(k)-26;                              
        end                                            
    end                                                
end                                                    
fprintf('�������K��G%s\n',s)                                
