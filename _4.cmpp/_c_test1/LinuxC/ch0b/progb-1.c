#include <stdio.h>
main(void)
{
 int i,limit,result=0;
 int getlim(void);
 limit=getlim();
 for (i=1;i<=limit;i++)
    result=result+i;
 printf("The result is %d\n", result);
}

int getlim(void)
{
 int rvalue;
 printf("Please input a value:");
 scanf("%d",&rvalue);
 return rvalue;
}
