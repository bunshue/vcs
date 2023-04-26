 #include <stdio.h>
 main(void)
 {
  union{
   int a;
   char b;
   float c;
   double d;
   } data1;

   printf("%d\n",sizeof(data1));
   printf("%x %x %x %x\n",&data1.a,&data1.b,&data1.c,&data1.d);
 }
