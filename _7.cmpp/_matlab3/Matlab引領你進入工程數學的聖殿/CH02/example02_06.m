sum1=0;sum2=0;                                                   
n=input('Enter the number of points�G');  % ���ܿ�J�ƭȭӼ�              
if n<2                                                           
    warning('MATLAB:Numberofinputs','At least 2 values needed.') 
else                                                             
    for k=1:n                                                    
       x=input('Enter values�G');                                 
       sum1=sum1+x;                                              
       sum2=sum2+x^2;                                            
    end                                                          
    xaver=sum1/n;  % �����ȭp�⤽��                                     
    s=sqrt((n*sum2-sum1^2)/(n*(n-1)));  % �Э�t�p�⤽��                
    disp(['�����ȡG',num2str(xaver),sprintf('\n'),'�Э�t�G',num2str(s)])
end                                                              
