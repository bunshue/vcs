 #include <stdio.h>
 main(void)
 {
  int x=10,y=20;
  void swap (int, int);
  swap(x,y);
  printf("x = %d,y = %d in main()\n",x,y);
 }

 void swap(int n1,int n2)
 {
  int temp;
    printf("x = %d,y = %d in swap() before swap\n",n1,n2);
    temp=n1;
    n1=n2;
    n2=temp;
    printf("x = %d,y = %d in swap() after swap\n",n1,n2);
 }
