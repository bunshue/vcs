 #include <stdio.h>
 main(void)
 {
      void my_printf(int s);
      int  i;
      i= 2;
      my_printf(i);
 }

 void my_printf(int s)
 {
   printf("Hi! C!\n");
   printf("This is my %dnd C program! ...",s);
   printf("OK?");
 }
