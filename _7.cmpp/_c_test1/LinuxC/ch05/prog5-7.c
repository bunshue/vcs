 #include <stdio.h>
 main(void)
 {
 int a,b,n;
 unsigned c=0x8000; /* c= 1000 0000 0000 0000 */
 unsigned d=0x0001; /* d= 0000 0000 0000 0001 */

 printf("a  b   a&b  a|b  a^b\n");
 for (a=0; a<=1; a++)
   for (b=0; b<=1; b++)
     printf("%d  %d    %d    %d    %d\n",a,b,a&b,a|b,a^b);

 for (n=0;n<8;n=n+1)
   printf("%04x shift right %d bit = %04x\n",c,n,c >> n);

 for (n=7;n>=0;n=n-1)
   printf("%04x shift left  %d bit = %04x\n",d,n,d << n);

 }
