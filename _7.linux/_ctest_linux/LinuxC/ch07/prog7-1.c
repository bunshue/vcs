 #include<stdio.h>
 main(void)
 {
  double  half(double),r;
  int  i;

  for (i=0; i<5; i++){
      r=half((double) i);
      printf("full=%d  half=%f\n",i,r);
      }
 }

 double  half(double s)
 {
  double  r;
  r=s/2;
  return  r;
 }
