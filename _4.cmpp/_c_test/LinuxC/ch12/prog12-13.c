 #include <sys/stat.h>
 #include <sys/types.h> 
 #include <stdio.h>
 main(void)
 {
  char pathname[100];
  printf ("Please input directory path:");
  scanf("%s", pathname);

  mkdir(pathname, 00400|00200|00040|00020);  
 }
