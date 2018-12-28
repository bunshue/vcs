 #include <stdio.h>
 main(void)
  {
   int    i;
   char   *pa;
   static char a[4]={'A', 'B', 'C', 'D'};
   pa = a;
   for ( i=0; i<4; i++)
       printf("a[%d]:%c  *(pa+%d):%c\n", i, a[i], i, *(pa+i));
  }
