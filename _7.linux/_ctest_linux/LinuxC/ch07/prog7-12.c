 #include <stdio.h>
 #include <stdlib.h>
 main( void )
 {
   unsigned int i;
   printf("Please input a seed:");
   scanf("d",&i);
   srand(i);
   printf("The RAND_MAX is:%d\n",RAND_MAX);
   for(i = 0; i < 10;i++ )
      printf("%5d\n", rand());
 }
