 #include <stdio.h>
 #define  ESC    27
 main(void)
 {
   int  key;
   while (1)
   { key=getchar();
     if (key != 10)
        printf("It's ASCII is %02x \n",key);
     if (key == ESC) 
        break;
   }
   printf("\nYou press <ESC> key !");
 }
