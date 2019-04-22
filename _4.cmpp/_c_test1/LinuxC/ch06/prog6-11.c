 #include <stdio.h>
 main(void)
 {
  float sum,i;

  for (sum=0.0,i=1.0;i<=10.0;sum+=i,i+=0.1)
     ;
  printf("sum = %f\n",sum);
 }
