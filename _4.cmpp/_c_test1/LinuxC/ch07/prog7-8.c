 #include <stdio.h>
 #define debug   1
 #define print_v printf("a= %d,b= %d ",a,b); \
                 printf("result =%d\n",result)
 main(void)
 {
  int a,b,result;
  printf("Input a and b = ");
  scanf("%d %d",&a,b);
  result = a * b + b * 3;

  if (debug) print_v;

  printf("Program end here.\n");
 }
