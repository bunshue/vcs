 #include <unistd.h> 
 #include <stdio.h>
 main(void)
 {
  char filename[100];
  printf ("Please input filename:");
  scanf("%s", filename);

  unlink(filename);  
 }
