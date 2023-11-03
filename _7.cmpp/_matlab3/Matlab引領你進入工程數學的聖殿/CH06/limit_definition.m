disp('==判斷常量A是否是函數f(x)在x0處的左極限==')       
A=input('請輸入可能極限值A=');                   
x0=input('請輸入極限點x0=');                   
f=input('請輸入極限表達式f(x)=','s');            
n=1;flag=1;delta=1;                      
x=x0-delta;                              
while flag==1                            
    epsilon=input('任意輸入一個任意小的數ε=');      
    while abs(eval(f)-A)>epsilon         
        delta=delta/2;                   
        x=x0-delta;                      
        if abs(delta)<eps                
            disp('找不到δ')                 
            n=0;break                    
        end                              
    end                                  
    if n==0                              
        disp('左極限不正確')                   
        break                            
    end                                  
    disp(['δ=',num2str(delta)])          
    flag=input('要重試一個ε嗎？重試按1，否則按其他數字鍵：');
end                                      
