 #include <unistd.h>
 #include <stdio.h>
 main(void)
 {
  char name[100];
  int len=100;
  gethostname(name,100);
  printf ("%s\n", name);
 }
