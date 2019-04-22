 #include <stdio.h>
 #define func(x) x*x+x*2+4
 main(void)
 {
  int a,result;
  printf("Please input a value : ");
  scanf("%d",&a);
  result=func(a);
  printf("func(x)=x*x+x*2+4\n");
  printf("func(%d)= %d\n",a,result);
 }
