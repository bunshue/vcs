 #include <stdio.h>
 main(void)
 {
 int x;
 int result,fact(int);
 while(1)
     {
       printf("input an integer number:");
       scanf("%d",&x);
       result=fact(x);
       printf("x = %d, result = %ld\n",x,result);
     }
 }

 int fact(int n)
 {
 if (n==0)
    return 1;
 else
    return( n*fact(n-1) );
 }
