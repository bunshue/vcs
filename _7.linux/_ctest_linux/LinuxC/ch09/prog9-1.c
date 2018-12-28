 #include<stdio.h>
 main(void)
 {
  int i,j=0;

  for (i=0; i<5; i++)
    {
     int j;
     if (i==0) j=0;
     j+=i;
     printf("j in for() block: %d\n",j);
    }
  j+=i;
  printf("j outside for() block: %d\n",j);
 }
