 #include <unistd.h>
 #include <stdio.h>
 main(void)
 {
  char pathname[100];
  getcwd(pathname, 100);

  printf("Working directory is %s", pathname);  
 }
