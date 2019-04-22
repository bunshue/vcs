 #include <sys/types.h>
 #include <sys/stat.h> 
 #include <stdio.h>
 main(void)
 {
  char filename[100];
  printf ("Please input filename:");
  scanf("%s", filename);

  chmod(filename, 00400|00200|00040|00004);  
 }
