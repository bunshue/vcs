 #include<stdio.h>
 void func(void);
 main(void)
 {
   int  i=1;
   func();
   printf("The value of i in main() = %d\n",i);
 }

 void func(void)
 {
   int  i=1;
   i--;
   printf("The value of i in func() = %d\n",i);
 }
