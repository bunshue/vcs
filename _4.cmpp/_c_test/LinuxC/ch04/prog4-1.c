 #include<stdio.h>
 main(void)
 {
   short i=0x4142;
   int j=0x43444546;

   printf("Size of short i  :%d\n",sizeof(i));
   printf("Size of int j :%d\n",sizeof(j));

   printf("%d\n",i);
   printf("%d\n",j);
 }
