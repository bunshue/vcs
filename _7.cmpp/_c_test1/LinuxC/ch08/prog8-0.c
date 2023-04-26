 #include <stdio.h>
 main(void)
 {
  int a=86;
  int *pa;
  pa = &a;
  printf("pa=%p, *pa=%d\n",pa,*pa);
  printf("&a=%p, a=%d\n",&a,a);
 }
