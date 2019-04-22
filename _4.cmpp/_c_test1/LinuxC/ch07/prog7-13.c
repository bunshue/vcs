 #include <stdio.h>
 #include <stdlib.h>
 #include <time.h>
 main( void )
 {
   unsigned int i;
   srand((unsigned) time(NULL));
   for(i = 0; i < 5;i++ )
      printf("%5d\n", rand());
 }
