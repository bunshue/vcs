 #include <stdio.h>
 main(void)
 {
  int i,sum=0;
  int s[7]= {1,-2,3,-4,5,-6,7 };

  for (i=0;i<7;i++)
     {
     if (s[i]<=0) continue;
     sum=sum+s[i];
     }
  printf("SUM = %d\n",sum);
 }
