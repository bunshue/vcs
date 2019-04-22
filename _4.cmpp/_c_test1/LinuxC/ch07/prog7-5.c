 #include <stdio.h>
 main(void)
 {
  int x,y;
  int result,power2(int,int);

  printf("Input x,y:");
  scanf("%d %d",&x,&y);
  result=power2(x,y);
  printf("x = %d y = %d,result = %ld\n",x,y,result);
 }

 int power2(int x,int y)
 {
   int z;
   printf("y= %d\n",y);
   if (y==1)
      return x;
   else
      if (y%2==0)
	{
         z= power2 (x,y/2);
         return z*z;
	}
      else
        return (x* power2(x,y-1));
 }
