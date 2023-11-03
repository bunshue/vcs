function hanoi(n,A,B,C)                              
%HANOI   梵塔問題                                        
% HANOI(N,'A','B','C')  遞歸算法求梵塔問題                    
%                                                    
% 輸導入參數數：                                              
%     ---N：碟的個數                                      
%     ---'A','B','C'：三個塔的名稱                          
                                                     
fprintf('%d個碟子的搬移步驟：\n',n)                           
count=1;                                             
move(n,A,B,C)                                        
    function move(n,A,B,C)                           
        if n==0                                      
            return                                   
        else                                         
            move(n-1,A,C,B)                          
            disp(['第',int2str(count),'步：',A,'-->',C])
            count=count+1;                           
            move(n-1,B,A,C)                          
        end                                          
    end                                              
end                                                  
