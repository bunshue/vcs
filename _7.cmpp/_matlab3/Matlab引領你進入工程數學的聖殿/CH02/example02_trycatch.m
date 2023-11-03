try                                                       
    index=input('Enter subscript of element to display¡G');
    disp(['a(',int2str(index),')=',num2str(a(index))])    
catch                                                     
    disp(['Illegal subscript¡G',int2str(index)])           
    A=lasterr;                                            
    disp(['Type of error¡G',A])                            
end                                                       
