 #include <stdio.h>
 #include <stdlib.h>
 #include <time.h>
 main( void )
 {
   void delay1(void),delay2(void);
   int begin,end;
   printf("Test my delay functions:\n");
   begin=clock();
   delay1();
   end=clock();
   printf("CLOCKS_PER_SEC = %d\n",CLOCKS_PER_SEC);
   printf("It took %d clock ticks (%g seconds) to run delay1()!\n",
       end-begin,(float)(end-begin)/CLOCKS_PER_SEC);
   begin=clock();
   delay2();
   end=clock();
   printf("It took %d clock ticks (%g seconds) to run delay2()!\n",
        end-begin,(float)(end-begin)/CLOCKS_PER_SEC);
 }

 void delay1()
 {
     int i;
     for (i=0;i<1E7;i++) ;
 }

 void delay2()
 {
     int i;
     for (i=0;i<1E7;i++)
       {
        i++;
	i--;
       }
 }
