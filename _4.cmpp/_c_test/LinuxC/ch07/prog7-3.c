 #include <stdio.h>
 main(void)
 {
  int x=3,y=12;
  int result,power(int,int);
  result=power(x,y);
  printf("x = %d y = %d,result = %ld\n",x,y,result);
 }

 int power(int x,int y)
 {
    if (y==1)
       return x;
    else
       return( x*power(x,y-1) );
 }
