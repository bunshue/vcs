 #include <stdio.h>
 void func(int *,int);

 main(void)
 {
  int a[5]={1,2,3,4,5};
  int n;

  printf("Before calling...\n");
  for (n=0;n<5;n++)
     printf("a[%d] = %d\n",n,a[n]);

  func(a,5);

  printf("After calling...\n");
  for (n=0;n<5;n++)
     printf("a[%d] = %d\n",n,a[n]);
 }

 void func(pointer,count)
 int *pointer;
 int count;
 {
  int m,buffer;
  for (m=0;m<count;m++,pointer++)
      {
      buffer=*pointer;
      buffer=buffer+1;
      *pointer=buffer;
      }
 }
