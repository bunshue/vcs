 #include <stdio.h>
 main(void)
 {
   int num1,num2,a,b,c;
   printf ("Input 2 numbers:");
   scanf("%ld %ld",&num1,&num2);
   c = num1%num2;
   b = num2;
   while (c>0)
   {
     a=b;
     b=c;
     c=a%b;
     printf ("a=%8ld, b=%8ld, c=%8ld\n",a,b,c);
   }

   printf("The g.c.d. of %ld and %ld is %ld\n",num1,num2,b);
  }
