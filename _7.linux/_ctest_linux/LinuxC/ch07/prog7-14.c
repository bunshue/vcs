 #include <stdio.h>
 #include <time.h>
 main( void )
 {
   long i;
   i=time(NULL);
   printf("There are %ld seconds since 1970-1-1 0:00:00\n", i);
 }
