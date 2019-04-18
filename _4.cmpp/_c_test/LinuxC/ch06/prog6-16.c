 #include <stdio.h>
 #define ESC     27
 main(void)
 {
   int i,key;
   for (i=0;i<20;i++)
       {
       printf("i= %2d ",i);
       key=getchar();
       if (key==ESC)
          {
           printf("You press <ESC> key\n");
           break;
          }
     }
   printf("It's over!\n");
 }
