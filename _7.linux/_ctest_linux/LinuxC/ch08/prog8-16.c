 #include <stdio.h>
 main(void)
 {
  char **pa;
  char *a[3];
  int n,m;
  pa=a;
  *(pa+0)="BOOK";
  *(pa+1)="YOU";
  *(pa+2)="LINUX";
  
  for (n=0;n<3;n++)
     {
      printf("\n pa+%d= %x\n",n,pa+n);
      printf(" addr of *(pa+%d)= %x\n",n,*(pa+n));
      printf(" string pointed by *(pa+%d)= %s\n",n,*(pa+n));
      for (m=0; *(*(pa+n)+m) !='\0';m++)
          printf("*(*(pa+%d)+%d)=%c ",n,m,*(*(pa+n)+m));
     }
 }
