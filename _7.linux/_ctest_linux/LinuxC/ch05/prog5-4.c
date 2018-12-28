 #include <stdio.h>
 main(void)
 {
   int a=8, b=6, c=3;

   printf("%d\n",a*b%c+2);
   printf("%d\n",++a*c-b--);
   printf("%d\n",a-((-c)*(++b)));
 }
