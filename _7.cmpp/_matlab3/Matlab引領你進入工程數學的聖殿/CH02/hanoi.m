function hanoi(n,A,B,C)                              
%HANOI   �����D                                        
% HANOI(N,'A','B','C')  ���k��k�D�����D                    
%                                                    
% ��ɤJ�ѼƼơG                                              
%     ---N�G�Ъ��Ӽ�                                      
%     ---'A','B','C'�G�T�Ӷ𪺦W��                          
                                                     
fprintf('%d�ӺФl���h���B�J�G\n',n)                           
count=1;                                             
move(n,A,B,C)                                        
    function move(n,A,B,C)                           
        if n==0                                      
            return                                   
        else                                         
            move(n-1,A,C,B)                          
            disp(['��',int2str(count),'�B�G',A,'-->',C])
            count=count+1;                           
            move(n-1,B,A,C)                          
        end                                          
    end                                              
end                                                  
