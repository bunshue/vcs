 #include <stdio.h>
 main(void)
 {
  float p=1234.56;
  float n=-456.78;

  printf("Value of p is:%10.2f!\n",p);
  printf("Value of p is:%10.5f!\n",p);
  printf("Value of p is:%10.1f!\n",p);
  printf("Value of p is:%10.7f!\n",p);
  printf("Value of p is:%-10.2f!\n",p);
  printf("Value of n is:%-10.2f!\n",n);
  printf("Value of p is:%+10.2f!\n",p);
  printf("Value of n is:%+10.2f!\n",n);
  printf("Value of p is:%+-10.2f!\n",p);
  printf("Value of n is:%+-10.2f!\n",n);
 }
