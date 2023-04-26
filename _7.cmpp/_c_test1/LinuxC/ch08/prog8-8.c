 #include <stdio.h>
 main(void)
 {
   int  *pa,i;
   static int a[4]={1, 2, 3, 4};
   pa = a;
   for ( i=0; i<4; i++)
       printf("&a[%d]:%x,  pa+%d:%x\n", i, &a[i], i, pa+i);
 }
