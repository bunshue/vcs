 #include <stdio.h>               
 typedef  char  (*ARRAYPTR)[10];  
 typedef  char  ARRAY[10];        
                                  
 main(void)                  
 {                                
   ARRAYPTR  ap;                  
   ARRAY     a;                   

   printf("INPUT A STRING:");     
   fgets(a,100,stdin);                       
   ap = &a;                       
   printf("\nECHO:%s\n", ap);     
 }
