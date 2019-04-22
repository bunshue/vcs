 #include<stdio.h>
 main(void)
 {
   int i;

   void inc(void);
   printf("static auto\t auto variable\n");
   for (i=0; i<5; i++)
        inc();
 }

 void inc(void)
 {
   static int counter1=0;
   int counter2=0;
   printf("counter1 = %d\t counter2 = %d \n",counter1,counter2);
   counter1++;
   counter2++;
 }
