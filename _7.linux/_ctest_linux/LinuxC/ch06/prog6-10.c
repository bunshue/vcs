 #include <stdio.h>
 main(void)
 {
  int count,delay;

  for (count=1;count<=3;count++)
      {
       printf("beep !\n");
       putchar(0x07); /* beep */
       for (delay=0;delay<6000000;delay++)
	   ;
      }
 }
