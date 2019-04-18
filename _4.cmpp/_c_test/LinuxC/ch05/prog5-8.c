 #include <stdio.h>
 main(void)
 {
 int i=512;

 printf("i/2 = %5d\n", i>>1);
 printf("i/4 = %5d\n", i>>2);
 printf("i/8 = %5d\n", i>>3);
 printf("i/16= %5d\n", i>>4);

 printf("i*2 = %5d\n", i<<1);
 printf("i*4 = %5d\n", i<<2);
 printf("i*8 = %5d\n", i<<3);
 printf("i*16= %5d\n", i<<4);
 }
