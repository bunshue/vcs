 #include <stdio.h>
 void swap(int *,int *);
 main(void)
 {
  int x=10,y=20;
  printf("x = %d,y =%d before call swap.\n",x,y);
  printf("The address of x is %x.\n",&x);
  printf("The address of y is %x.\n",&y);
  swap(&x,&y);
  printf("x= %d,y =%d after call swap.\n",x,y);
 }

 void swap(int *px,int *py)
 {
  int temp;
  temp=*px; /* x value pass to temp */
  *px=*py;  /* y value pass to x    */
  *py=temp; /* temp pass to y */
 }
