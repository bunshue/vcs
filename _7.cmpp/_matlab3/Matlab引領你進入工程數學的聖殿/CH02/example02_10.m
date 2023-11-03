fprintf('==比賽名單==\n')                                         
for i='X':'Z'                                                 
    for j='X':'Z'                                             
        for k='X':'Z'                                         
            if ~isequal(i,j) && ~isequal(i,k) && ~isequal(j,k)
                if i~='X'&&k~='X'&&k~='Z'                     
                    fprintf('%c vs %c\n',['A','B','C';i,j,k]) 
                end                                           
            end                                               
        end                                                   
    end                                                       
end                                                           
