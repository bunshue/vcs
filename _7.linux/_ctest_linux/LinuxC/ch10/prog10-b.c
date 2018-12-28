 #include <stdio.h>                                   
 struct word { unsigned bit0 : 1;                    
               unsigned bit1 : 1;                    
               unsigned bit2 : 1;                    
               unsigned bit3 : 1;                    
               unsigned status : 4;                  
             } flag;                                 
                                                     
 main(void)                                     
 {                                                   
         printf("Input a number (2 digits) in HEX :");
         scanf("%2x",&flag);                         
         printf("Bit0 =%x\n",flag.bit0);             
         printf("Bit1 =%x\n",flag.bit1);             
         printf("Bit2 =%x\n",flag.bit2);             
         printf("Bit3 =%x\n",flag.bit3);             
         printf("Status=%x\n",flag.status);          
 }                                                   
