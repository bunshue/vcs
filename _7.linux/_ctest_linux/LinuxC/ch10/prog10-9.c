 #include<stdio.h>
 main(void)
 {
  union {
         int  a;
         char b;
        } data;

  data.a=0x12000000;
  printf("data.a = %04x\n",data.a);
  data.b=0x33;
  printf("data.b = %c\n",data.b);
  printf("data.a = %04x\n",data.a);
 }
