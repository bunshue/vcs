 #include <stdio.h>
 main(void)
 {
 int i=0,sum=0;
 while (i<30)
   {
   i++;
   if (i%3 != 0) continue;
   sum += i;
   }
 printf("SUM = %d\n",sum);
 }
