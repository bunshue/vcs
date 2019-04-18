 #include <stdio.h>
 #include <math.h>
 main(void)
 {
  float x,y;
  printf("Please input a number:");
  scanf("%f", &x);

  printf(" square root of %f is %g\n", x, sqrt (x));
  printf(" sin(%f*PI) =  %g\n", x,sin(x*M_PI));
 }
