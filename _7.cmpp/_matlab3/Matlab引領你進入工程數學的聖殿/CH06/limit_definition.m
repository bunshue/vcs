disp('==�P�_�`�qA�O�_�O���f(x)�bx0�B��������==')       
A=input('�п�J�i�෥����A=');                   
x0=input('�п�J�����Ix0=');                   
f=input('�п�J������F��f(x)=','s');            
n=1;flag=1;delta=1;                      
x=x0-delta;                              
while flag==1                            
    epsilon=input('���N��J�@�ӥ��N�p���ƣ`=');      
    while abs(eval(f)-A)>epsilon         
        delta=delta/2;                   
        x=x0-delta;                      
        if abs(delta)<eps                
            disp('�䤣��_')                 
            n=0;break                    
        end                              
    end                                  
    if n==0                              
        disp('�����������T')                   
        break                            
    end                                  
    disp(['�_=',num2str(delta)])          
    flag=input('�n���դ@�ӣ`�ܡH���ի�1�A�_�h����L�Ʀr��G');
end                                      
