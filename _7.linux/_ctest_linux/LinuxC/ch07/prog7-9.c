 #include <stdio.h>
 #define DEBUG
 main(void)
 {
  int a,b,result;
  printf("Input a = ");
  scanf("%d",&a);
  printf("Input b = ");
  scanf("%d",&b);
  printf("result = a * b + b * 3\n");
  result = a * b + b * 3;

  #ifdef  DEBUG
         printf("a= %d b= %d , result = %d\n",a,b,result);
  #else 
         printf("result = %d\n",result);
  #endif
         printf("Program end here.\n");
 }
