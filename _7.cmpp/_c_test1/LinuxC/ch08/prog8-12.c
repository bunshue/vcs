 #include<stdio.h>
 main(void)
 {
  char a[10]="abcdefghi";
  char *p,*end;
  p=a;
  end=&a[9];
  while (p<end)
      printf("%c",*p++);
  printf("\n");
 }
