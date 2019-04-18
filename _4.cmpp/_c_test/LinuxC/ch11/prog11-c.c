 #include <stdio.h>
 main(void)
 {
  char c[15]="";
  unsigned int ret;
  ret=fread(c,1,14,stdin);

  puts(c);
  printf("%d character(s)\n",ret);
 }
