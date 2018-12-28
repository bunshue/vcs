 #include <stdio.h>
 #include <stdlib.h>
 main(int argc,char *argv[])
 {
  int n1,n2,sum;
  if (argc==3)
    {
     n1=atoi(argv[1]); /* call ASCII to integer */
     n2=atoi(argv[2]);
     sum=n1+n2;
     printf("%d(num1) + %d(num2) = %d\n",n1,n2,sum);
    }
 }
