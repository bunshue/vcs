 #include <stdio.h>
 #include <math.h>
 main(void)
 {
  double x,y;
  printf("I can compute x raised to the y power for you.\n");
  do
  {
    printf("Please input x and y:");
    scanf("%lf %lf", &x, &y);
    printf("%g raised to the %g power is %g\n\n",x,y,pow(x,y));
  }  while (x!=0) ;
 }
