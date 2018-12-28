 #include<stdio.h>
 main(void)
 {
  int i,j,k,avr1;
  float a,b,c,avr2;
  i=a=2;
  j=b=3;
  k=c=5;

  avr1=(i+j+k)/3;
  avr2=(i+j+k)/3;
  printf("avr1=%d\n",avr1);
  printf("avr2=%g\n\n",avr2);

  avr1=(i+j+k)/3.0;
  avr2=(i+j+k)/3.0;
  printf("avr1=%d\n",avr1);
  printf("avr2=%g\n\n",avr2);

  avr1=(a+b+c)/3;
  avr2=(a+b+c)/3;
  printf("avr1=%d\n",avr1);
  printf("avr2=%g\n\n",avr2);
 }
