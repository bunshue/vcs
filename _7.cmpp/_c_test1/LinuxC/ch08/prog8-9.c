 #include<stdio.h>
 main(void)
 {
  char a[10]="abcdefghi";
  char *one,*two;
  one=a;
  two=&a[5];
  printf("one[5]=%c two[3]=%c\n",one[5],two[3]);
  printf("*(a+5)=%c *(a+8)=%c\n",*(a+5),*(a+8));
 }
